import sys

sys.path.append("./dockerfileVulnerability")
from compose.compose_vulnerability_detection import get_compose_file_vulnerabilities
from dockerfileVulnerability.dockerfile_vulnerability_detection import get_dockerfile_vulnerabilities
from utils.file_extension import get_file_extension, get_filename
iac_file_path = './Dockerfile'

if get_file_extension(iac_file_path) == "Dockerfile" or get_filename(iac_file_path) == "Dockerfile" :
    get_dockerfile_vulnerabilities(iac_file_path)
else:
    get_compose_file_vulnerabilities(iac_file_path)