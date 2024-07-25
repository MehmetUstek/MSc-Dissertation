import re
from utils.file_extension import get_file_extension
from utils.extension_enum import Extension


def is_dockerfile(filename):
    """
    Check if a given filename is a Dockerfile. This function recognizes Dockerfiles named:
    - Exactly 'Dockerfile'
    - With a suffix, as in 'Dockerfile.prod' or 'Dockerfile.dev'
    - With a prefix, as in 'prod.Dockerfile' or 'dev.Dockerfile'
    
    Args:
    filename (str): The filename to check.
    
    Returns:
    bool: True if the filename is a Dockerfile, False otherwise.
    """
    # Check for exact match
    if filename == "Dockerfile":
        return True

    # Check for 'Dockerfile.' prefix with additional characters
    if filename.startswith("Dockerfile.") and len(filename) > len("Dockerfile."):
        return True

    # Check for '.Dockerfile' suffix with leading characters
    if filename.endswith(".Dockerfile") and len(filename) > len(".Dockerfile"):
        return True

    return False

def is_compose_yaml_file(filename):
    """
    Checks if the provided filename indicates it might be a Docker Compose file.
    This version accepts any filename containing 'compose' with a '.yaml' extension.
    
    Parameters:
        filename (str): The name of the file to check.
        
    Returns:
        bool: True if the filename contains 'compose' and ends with '.yaml', otherwise False.
    """
    # Regular expression to check for 'compose' in the filename and a '.yaml' extension
    pattern = r'compose.*\.(yaml|yml)$'
    
    # Use re.search to find 'compose' anywhere in the filename followed by '.yaml'
    return bool(re.search(pattern, filename, re.IGNORECASE))

def is_terraform(filename):
    return get_file_extension(filename) == ".tf"

def get_file_type(filename):
    if is_dockerfile(filename):
        return Extension.Dockerfile
    elif is_compose_yaml_file(filename):
        return Extension.Compose
    elif is_terraform(filename):
        return Extension.Terraform
    else:
        return None