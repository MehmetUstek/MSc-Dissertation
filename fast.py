import base64
import os

from fastapi import FastAPI, HTTPException, Request, logger
from fastapi.responses import JSONResponse
from single_file_vulnerability_scan.get_single_file_vulnerability import \
    get_single_file_vulnerability_filecontent
from pydantic import BaseModel
from utils.check_file_extensions import get_file_type
from utils.load_json_based_on_extension_type import \
    load_json_based_on_extension_type

# Now you can access the variables from the file as environment variables
debug = os.getenv('DEBUG', 'False') == "True"
# Determine environment from an environment variable
env = os.getenv('ENVIRONMENT', 'development')

# Enable documentation only in development
docs_url = "/docs" if env == 'development' else None
redoc_url = "/redoc" if env == 'development' else None

app = FastAPI(docs_url=docs_url, redoc_url=redoc_url)

class File(BaseModel):
    name: str
    content: str

class UnicornException(Exception):
    def __init__(self, message=None, http_status=500):
        super().__init__(message)
        self.message = message if message else "Unicorn Exception occurred."
        self.http_status = http_status


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    logger.logger.error(f"Handled UnicornException: {exc.message}")
    return JSONResponse(
        status_code=exc.http_status,
        content={"message": f" {exc.http_status}. The file is not available for vulnerability scanning."}
    )


# Middleware to block all paths except the allowed one
@app.middleware("http")
async def block_other_paths(request: Request, call_next):
    if request.url.path == "/vulnerability_scan/":
        response = await call_next(request)
        return response
    else:
        if debug:
            response = await call_next(request)
            return response
        raise HTTPException(status_code=404, detail="Not Found")


@app.post("/vulnerability_scan/")
async def vulnerability_scan(file: File):
    try:
        original_content = base64.b64decode(file.content.encode('utf-8')).decode('utf-8')
        if original_content:
            # print("Original Content:", original_content)
            # print("Filename:", file.name)
            extension = get_file_type(filename=file.name)
            if extension:
                try:
                    json_data = get_single_file_vulnerability_filecontent(
                        file_content=original_content, file_extension=extension, 
                        filename=file.name, baseImageScan=False
                    )
                    if json_data:
                        error_descriptions = load_json_based_on_extension_type(extension)
                        # print("Vulnerability Details:", json_data)

                        for item in json_data:
                            # print("Vulnerability Item:", item)
                            item["errorNo"] = error_descriptions[item["errorNo"]]
                        return json_data
                    else:
                        return JSONResponse(
                        status_code=250,
                        content={"message":"File contains no vulnerabilities."}
                        )
                except RuntimeError as re:
                    # print(f"Error reading the file: {str(re)}")
                    raise UnicornException(http_status=574, message="Syntax error in the file")
                except Exception as e:
                    raise
                
            else:
                raise UnicornException(http_status=571, message="Unknown file extension.")
        else:
            raise UnicornException(http_status=573, message="Empty file content, or inccorect base64 padding")
    except UnicornException as ue:
        # print(f"Error ({ue.http_status}): {ue.message}")
        raise




# 250: No vulnerabilities in the file.
# 571: File extension is not valid for vulnerability scanning. Use one of dockerfile, compose, or terraform files for this extension.
# 572: The file content has invalid syntax.
# 573: Incorrect base64 padding.