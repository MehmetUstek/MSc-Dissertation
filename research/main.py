import argparse
import os

from research.get_directory_vulnerability import get_directory_file_vulnerability
from single_file_vulnerability_scan.get_single_file_vulnerability import \
    get_single_file_vulnerability_filepath

## Run
# Compose at local: python3 main.py -f compose.yaml
# Dockerfile at local: python3 main.py -f Dockerfile

def main():
    parser = argparse.ArgumentParser(description="AST-matching IaC configuration file vulnerability scanner", add_help=True)
    parser.add_argument('-bis', '--baseImageScan', type=bool, help='Base Image Scan, false by default', required=False, default=False)
    parser.add_argument('--analytics', action='store_true', help='Analytics, false by default', required=False, default=False)
    parser.add_argument('-vb','--verbose', action='store_true', help='verbose', required=False, default=False)
    parser.add_argument('-fL','--fileLimit', type=int, help='Directory File Limit', required=False, default=1000)
    parser.add_argument('--debug', action='store_true', help='Debug, false by default', required=False, default=False)
    parser.add_argument('--vulnerabilityList', action='store_true', help='Vulnerabilities returned as a list, false by default', required=False, default=False)
    parser.add_argument('--generateVulnerabilityList', action='store_true', help='Vulnerabilities returned as a list, false by default', required=False, default=False)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help='Absolute file path to process IaC configuration file', required=False)
    group.add_argument('-d', '--directory', type=str, help='Absolute directory path to process IaC configuration file', required=False)

    # parser.add_argument('-js','--returnJson', type=bool, help='Output format of the vulnerabilities', required=False, default=False)
    
    args = parser.parse_args()
    # print("args", args)

    try:
        if args.directory:
            print(f"The provided directory path is: {args.directory}")
            directory_path = args.directory
            analytics = args.analytics
            directory_file_limit = args.fileLimit
            verbose = args.verbose
            get_directory_file_vulnerability(os.path.abspath(directory_path),analytics, directory_file_limit=directory_file_limit,isVerbose=verbose)
        elif args.file:
            print(f"The provided file path is: {args.file}")
            file_path = args.file
            debug = args.debug
            vulnerabilities = get_single_file_vulnerability_filepath(os.path.abspath(file_path), baseImageScan=args.baseImageScan, debug= debug)
            if vulnerabilities and args.vulnerabilityList:
                # print(vulnerabilities)
                all_errorNos = [int(entry['errorNo']) for entry in vulnerabilities]
                print(all_errorNos)
        else:
            print("No file or directory specified.")
    except:
        raise
    

if __name__ == "__main__":
    main()
