# Security Vulnerability Detection in IaC Configuration Files

This tool is designed to identify vulnerabilities in Docker Compose files and Dockerfiles. It can analyze individual files or entire directories to detect potential security issues.

## Features

- **Directory Scanning**: Recursively scan all Docker-related files in a specified directory.
- **Docker Compose Vulnerability Detection**: Analyze Docker Compose files for known vulnerabilities.
- **Dockerfile Vulnerability Detection**: Scan Dockerfiles, optionally including base image scans, for known vulnerabilities.

## Requirements

- Python 3.x
- Necessary Python libraries: [requirements.txt](./requirements.txt)

## Usage

### Analyzing a Single File

You can analyze a specific file by providing its path. Use the following commands based on the file type:

- **For Dockerfiles**:
  ```bash
  python3 main.py -f /path/to/Dockerfile
  python -m research.main -f /path/to/Dockerfile
  ```
- **For Docker Compose files**:

  ```bash
  python3 main.py -f /path/to/compose.yaml
  python -m research.main -f /path/to/compose.yaml
  ```

  - **For Terraform files**:

  ```bash
  python3 main.py -f /path/to/terraform.tf
  python -m research.main -f /path/to/terraform.tf
  ```

- **For Entire directory scans**:
  ```bash
  python3 main.py -d /path/to/directory
  python -m research.main -d /path/to/directory
  ```

# References

This study benefited from TFSec (https://aquasecurity.github.io/tfsec/v1.28.1/checks/), and registry hashicorp terraform documentation (https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/) for research on terraform vulnerabilities, explanations, possible impacts and consequences.
