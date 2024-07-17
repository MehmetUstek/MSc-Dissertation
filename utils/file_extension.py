from pathlib import Path

def get_file_extension(filename):
    # Create a Path object and get the suffix
    return Path(filename).suffix

def get_filename(filename):
    # Create a Path object and get the suffix
    return Path(filename).name
