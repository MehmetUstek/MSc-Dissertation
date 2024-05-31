import json
import numpy as np
import logging

def flatten_json(json_data):
    # Flatten the JSON data
    # print("json_data", json_data)
    flattened_json_list = []
    for key, value in json_data.items():
        print("key,val", key, value)
        flattened_json_list.append(key)
        if isinstance(value, dict):
            flattened_json_list.extend(flatten_json(value))
        
    print("final flattened_json", flattened_json_list)
    return flattened_json_list

def extract_keys(data, prefix=''):
    """
    Recursively extract all keys from nested JSON-like dictionary.
    """
    keys = []
    for key, value in data.items():
        # Formulate a prefixed key to handle nested dictionaries uniquely
        composite_key = f"{prefix}.{key}" if prefix else key
        keys.append(composite_key)
        
        # If the value is a dictionary and not empty, recurse into it
        if isinstance(value, dict) and value:
            keys.extend(extract_keys(value, composite_key))
    return keys

# Load JSON data
with open('./compose_keys.json', 'r') as file:
    data = json.load(file)

# Extract all unique keys
all_keys = extract_keys(data)
all_keys = list(set(all_keys))  # Remove duplicates if any
print(all_keys)


def cosine_similarity(vec1, vec2):
    """Calculate the cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    print("vec1",vec1)
    # print("vec2",vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

def flatten_dict(d, parent_key='', sep='_'):
    """
    Recursively flatten a dictionary and handle nested lists and dictionaries.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}{sep}{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

def one_hot_encode_ast(ast, all_keys):
    """
    One-hot encode a Docker Compose AST or any part of it based on a list of all possible keys.
    """
    vector = [0] * len(all_keys)  # Initialize vector with zeros
    flattened_ast = flatten_dict(ast)  # Flatten the AST to handle nested structures
    print("flattened_ast",flattened_ast)
    
    for key, value in flattened_ast.items():
        composite_key = f"{key}_{value}"  # Create a composite key from key and value
        print("composite_key",composite_key)
        if key in all_keys:
            print("key,val", key, value)
            index = all_keys.index(key)
            vector[index] = 1
    return vector





logging.basicConfig(level=logging.INFO)

def traverse_and_compare(ast, vulnerability_vector, all_keys, depth=0, path=''):
    """
    Recursively traverses an AST, applies one-hot encoding, compares each branch to a vulnerability vector,
    and logs a warning if the similarity exceeds a threshold.
    
    :param ast: AST node currently being traversed.
    :param vulnerability_vector: One-hot encoded vector representing a known vulnerability pattern.
    :param all_keys: List of all possible keys for one-hot encoding.
    :param depth: Current depth in the AST (used for structured logging).
    :param path: Path string for logging purposes.
    """
    if isinstance(ast, dict):
        for key, subtree in ast.items():
            new_path = f"{path}.{key}" if path else key
            if isinstance(subtree, dict):
                traverse_and_compare(subtree, vulnerability_vector, all_keys, depth+1, new_path)
            else:
                # Apply one-hot encoding to the current subtree and compare
                branch_vector = one_hot_encode_ast(ast, all_keys)
                similarity = cosine_similarity(branch_vector, vulnerability_vector)
                if similarity > 0.85:
                    logging.warning(f"High similarity ({similarity}) found in branch {new_path}")
    elif isinstance(ast, list):
        for idx, item in enumerate(ast):
            new_path = f"{path}[{idx}]"
            traverse_and_compare(item, vulnerability_vector, all_keys, depth+1, new_path)

# Example usage
# Define all_keys as extracted previously
# Define vulnerability_vector as a one-hot encoded vector of a known vulnerability
ast_example = {
    "services": {
        "web": {
            "image": "nginx",
        },
        "db": {
            "image": "postgres"
        }
    }
}

all_keys_list = flatten_json(data)
print("fltten", all_keys_list)

antipattern_example = {"services":{ "image": ":latest" }}
antipattern_vector =  one_hot_encode_ast(antipattern_example, all_keys_list)
print("antipattern_vector",antipattern_vector)

# Start the traversal and comparison
traverse_and_compare(ast_example, antipattern_vector, all_keys_list)
