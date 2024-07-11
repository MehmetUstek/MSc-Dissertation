import base64

from fastapi import FastAPI, HTTPException
from get_single_file_vulnerability import \
    get_single_file_vulnerability_filecontent
from pydantic import BaseModel
from utils import load_json

app = FastAPI()

class File(BaseModel):
    name: str
    content: str

@app.post("/vulnerability_scan/")
async def vulnerability_scan(file:File):
    original_content = base64.b64decode(file.content.encode('utf-8')).decode('utf-8')
    print(original_content)
    print("filename", file.name)
    json_data = get_single_file_vulnerability_filecontent(file_content= original_content,filename=file.name,
                                                           baseImageScan=False)
    error_descriptions = load_json('dockerfileVulnerability/antipattern_descriptions.json')
    print("json_data",json_data)

    for item in json_data:
        print("item", item)
        item["errorNo"] = error_descriptions[item["errorNo"]]
    return json_data
