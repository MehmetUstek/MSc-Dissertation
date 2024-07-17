import base64

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from get_single_file_vulnerability import \
    get_single_file_vulnerability_filecontent
from pydantic import BaseModel
from utils.load_json_based_on_extension_type import load_json_based_on_extension_type
from utils.check_file_extensions import get_file_type
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class File(BaseModel):
    name: str
    content: str

class UnicornException(Exception):
    def __init__(self, exception_code: int):
        self.exception_code = exception_code


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=exc.exception_code,
        content={"message": f"Oops! {exc.exception_code}. The file is not available for vulnerability scanning."}
    )


@app.post("/vulnerability_scan/")
async def vulnerability_scan(file:File):
    original_content = base64.b64decode(file.content.encode('utf-8')).decode('utf-8')
    print(original_content)
    print("filename", file.name)
    extension = get_file_type(filename=file.name)
    if extension:
        
        json_data = get_single_file_vulnerability_filecontent(file_content= original_content,file_extension=extension, filename=file.name, 
                                                            baseImageScan=False)
        if json_data:
            if len(json_data) > 0:
                error_descriptions = load_json_based_on_extension_type(extension)
                print("json_data",json_data)

                for item in json_data:
                    print("item", item)
                    item["errorNo"] = error_descriptions[item["errorNo"]]
                return json_data
        else:
            raise UnicornException(exception_code=572)
    else:
        raise UnicornException(exception_code=571)

# 571: File extension is not valid for vulnerability scanning. Use one of dockerfile, compose, or terraform files for this extension.
# 572: The fıle content has invalid syntax.