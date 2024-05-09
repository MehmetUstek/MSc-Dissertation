import json
import sys
sys.path.append("..")

def load_json(file_path):
    """Loads JSON data from a specified file path and returns it."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")