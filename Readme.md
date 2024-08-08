# Security Vulnerability Detection in IaC Configuration Files

This tool is designed to identify vulnerabilities in Docker Compose files and Dockerfiles. It can analyze individual files or entire directories to detect potential security issues.

## You can try it on VSCode!

[![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/MehmetUstek.iac-file-vulnerability-scan)](https://marketplace.visualstudio.com/items?itemName=MehmetUstek.iac-file-vulnerability-scan)

## Features

Speeds up the configuration vulnerability scan with a novel AST-matching technique

IaC configuration file vulnerability scan for:</br>

- **Dockerfiles**</br>
- **Compose.yaml/compose.yml Files**</br>
- **Terraform configuration files (.tf)**

**Directory Scanning**: Recursively scan all Docker-related files in a specified directory.</br>
**Terraform Vulnerability Detection**: Analyze Terraform configuration files for known vulnerabilities.</br>
**Docker Compose Vulnerability Detection**: Analyze Docker Compose files for known vulnerabilities.</br>
**Dockerfile Vulnerability Detection**: Scan Dockerfiles, optionally including base image scans, for known vulnerabilities.</br>

## Requirements

- Python 3.x, python 3.11 suggested
- Necessary Python libraries: [requirements.txt](./requirements.txt)

## Usage

### Analyzing a Single File

You can analyze a specific file by providing its path. Use the following commands based on the file type:

- **For Dockerfiles**:
  ```bash
  python -m research.main -f /path/to/Dockerfile
  ```
- **For Docker Compose files**:

  ```bash
  python -m research.main -f /path/to/compose.yaml
  ```

  - **For Terraform files**:

  ```bash
  python -m research.main -f /path/to/terraform.tf
  ```

- **For Entire directory scans**:
  ```bash
  python -m research.main -d /path/to/directory
  ```

# References

This study benefited from TFSec (https://aquasecurity.github.io/tfsec/v1.28.1/checks/), and registry hashicorp terraform documentation (https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/) for research on terraform vulnerabilities, explanations, possible impacts and consequences.
