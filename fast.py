import base64
import json
from fastapi import FastAPI, HTTPException
from get_single_file_vulnerability import get_single_file_vulnerability_filecontent
from pydantic import BaseModel

app = FastAPI()

class File(BaseModel):
    name: str
    content: str

@app.post("/vulnerability_scan/")
async def vulnerability_scan(file:File):
    # TODO: Change the file extension.
    original_content = base64.b64decode(file.content.encode('utf-8')).decode('utf-8')
    print(original_content)
    json_data = get_single_file_vulnerability_filecontent(file_content= original_content,file_extension="Dockerfile", baseImageScan=False)
    print(json_data)
    # json_payload = json.dumps(json_data)
    return json_data
