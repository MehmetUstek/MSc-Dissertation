from compose.compose_vulnerability_detection import get_compose_file_vulnerabilities
from dockerfileVulnerability.dockerfile_vulnerability_detection import get_dockerfile_vulnerabilities
from compose.vectorapproach2 import vectoral_scan
from utils.file_extension import get_file_extension, get_filename
import argparse
import os


## Run
# Compose at local: python3 main.py -f compose.yaml
# Dockerfile at local: python3 main.py -f Dockerfile

def get_single_file_vulnerability(file_path, baseImageScan = False):
    if get_file_extension(file_path) == ".Dockerfile" or get_filename(file_path) == "Dockerfile" :
        get_dockerfile_vulnerabilities(file_path,baseImageScan)
    else:
        # get_compose_file_vulnerabilities(file_path)
        vectoral_scan(file_path)


def get_directory_file_vulnerability(directory_path):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Print the names of each file
    for file in files:
        file_absolute_path = os.path.join(directory_path, file)
        print(file_absolute_path)
        get_single_file_vulnerability(file_absolute_path)


def main():
    parser = argparse.ArgumentParser(description="AST-matching IaC configuration file vulnerability scanner", add_help=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help='Absolute file path to process IaC configuration file', required=False)
    group.add_argument('-d', '--directory', type=str, help='Absolute directory path to process IaC configuration file', required=False)
    parser.add_argument('-bis', '--baseImageScan', type=bool, help='Base Image Scan, false by default', required=False, default=False)
    
    args = parser.parse_args()

    # Here, you can add the code to handle or process the file
    if args.directory:
        print(f"The provided directory path is: {args.directory}")
        directory_path = args.directory
        get_directory_file_vulnerability(os.path.abspath(directory_path))
    elif args.file: 
        print(f"The provided file path is: {args.file}")
        file_path = args.file
        get_single_file_vulnerability(os.path.abspath(file_path), args.baseImageScan)
    else:
        print("No file or directory specified.")
    

if __name__ == "__main__":
    main()
