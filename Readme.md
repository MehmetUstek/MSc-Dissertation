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
  ```
- **For Docker Compose files**:

  ```bash
  python3 main.py -f /path/to/compose.yaml
  ```

- **For Entire directory scans**:
  ```bash
  python3 main.py -d /path/to/directory
  ```
