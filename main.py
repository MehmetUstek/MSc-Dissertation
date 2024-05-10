from compose.compose_vulnerability_detection import get_compose_file_vulnerabilities
from dockerfileVulnerability.dockerfile_vulnerability_detection import get_dockerfile_vulnerabilities
from utils.file_extension import get_file_extension, get_filename
import argparse

## Run
# Compose at local: python3 main.py -f compose.yaml
# Dockerfile at local: python3 main.py -f Dockerfile

def main():
    parser = argparse.ArgumentParser(description="Process some file paths.")
    parser.add_argument('-f', '--file', type=str, help='File path to process', required=True)
    
    args = parser.parse_args()

    # Here, you can add the code to handle or process the file
    print(f"The provided file path is: {args.file}")
    iac_file_path = args.file
    if get_file_extension(iac_file_path) == "Dockerfile" or get_filename(iac_file_path) == "Dockerfile" :
        get_dockerfile_vulnerabilities(iac_file_path)
    else:
        get_compose_file_vulnerabilities(iac_file_path)

if __name__ == "__main__":
    main()
