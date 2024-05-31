from collections import Counter, defaultdict
from compose.compose_vulnerability_detection import get_compose_file_vulnerabilities
from dockerfileVulnerability.dockerfile_vulnerability_detection import get_dockerfile_vulnerabilities
from analytics.analytics import most_frequent_vulnerabilities_in_files
from utils.file_extension import get_file_extension, get_filename
import argparse
import os


## Run
# Compose at local: python3 main.py -f compose.yaml
# Dockerfile at local: python3 main.py -f Dockerfile

def get_single_file_vulnerability(file_path, baseImageScan = False, isVerbose = True):
    if get_file_extension(file_path) == ".Dockerfile" or get_filename(file_path) == "Dockerfile" :
        return get_dockerfile_vulnerabilities(file_path, baseImageScan, isVerbose=isVerbose)
    else:
        return get_compose_file_vulnerabilities(file_path, isVerbose=isVerbose)
        # vectoral_scan(file_path)


def get_directory_file_vulnerability(directory_path, isAnalytics, directory_file_limit, isVerbose):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Print the names of each file
    fileunique_vulnerability_counts = Counter()
    vulnerability_counts = defaultdict(int)
    severity_weighted_count = defaultdict(int)
    counter = 0

    for file in files:
        if counter >= directory_file_limit:
            break
        file_absolute_path = os.path.join(directory_path, file)
        print(file_absolute_path)
        vulnerabilities = get_single_file_vulnerability(file_absolute_path,isVerbose=isVerbose)
        # error_counts = Counter(error["errorNo"] for error in vulnerabilities)
        # print(error_counts)
        unique_errors = set()  # Set to track unique errorNos in the current file
        for vulnerability in vulnerabilities:
            unique_errors.add(vulnerability["errorNo"])
            vulnerability_counts[vulnerability["errorNo"]] += 1
            severity_weighted_count[vulnerability["errorNo"]] += vulnerability["severity"]

        for error_no in unique_errors:
            fileunique_vulnerability_counts[error_no] += 1
        counter += 1

    if isAnalytics:
        most_frequent_vulnerabilities_in_files(fileunique_vulnerability_counts, "Unique Error Numbers Across Files")
        most_frequent_vulnerabilities_in_files(vulnerability_counts, "Non-Unique Error Numbers Across Files")
        most_frequent_vulnerabilities_in_files(severity_weighted_count, "Weighted Non-Unique Error Numbers Across Files")
        


def main():
    parser = argparse.ArgumentParser(description="AST-matching IaC configuration file vulnerability scanner", add_help=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help='Absolute file path to process IaC configuration file', required=False)
    group.add_argument('-d', '--directory', type=str, help='Absolute directory path to process IaC configuration file', required=False)
    parser.add_argument('-bis', '--baseImageScan', type=bool, help='Base Image Scan, false by default', required=False, default=False)
    parser.add_argument('--analytics', type=bool, help='Analytics, false by default', required=False, default=False)
    parser.add_argument('-vb','--ver', type=bool, help='ver', required=False, default=False)
    parser.add_argument('-fL','--fileLimit', type=int, help='Directory File Limit', required=False, default=1000)
    
    args = parser.parse_args()
    print("args", args)

    # Here, you can add the code to handle or process the file
    if args.directory:
        print(f"The provided directory path is: {args.directory}")
        directory_path = args.directory
        analytics = args.analytics
        directory_file_limit = args.fileLimit
        verbose = args.ver
        get_directory_file_vulnerability(os.path.abspath(directory_path),analytics, directory_file_limit=directory_file_limit,isVerbose=verbose)
    elif args.file: 
        print(f"The provided file path is: {args.file}")
        file_path = args.file
        get_single_file_vulnerability(os.path.abspath(file_path), args.baseImageScan)
    else:
        print("No file or directory specified.")
    

if __name__ == "__main__":
    main()
