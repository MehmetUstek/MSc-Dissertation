# Root: Docker Compose File
    # Branch: version
    #   Leaf: '3.8'
    # Branch: services
    #   Sub-branch: webapp
    #       Leaf: image: webapp:latest
    #       Branch: ports
    #           Leaf: "5000:5000"
    #       Branch: depends_on
    #           Leaf: db
    #   Sub-branch: db
    #       Leaf: image: postgres:12
    #       Branch: volumes
    #           Leaf: db-data:/var/lib/postgresql/data
    # Branch: volumes
    #   Leaf: db-data

import yaml
from pprint import pprint

# def parse_yaml_to_ast(filename):
#     with open(filename, 'r') as file:
#         yaml_content = yaml.safe_load(file)
#         return create_ast(None, yaml_content)

# class ComposeNode:
#     """Represents a node in the Docker Compose AST."""
#     def __init__(self, key, value):
#         self.key = key  # This could be 'services', 'volumes', 'networks', etc.
#         self.value = value  # This could be a dict, list, or terminal value
#         self.children = []  # List of ComposeNode

#         if isinstance(value, dict):
#             for subkey, subvalue in value.items():
#                 self.children.append(ComposeNode(subkey, subvalue))
#         elif isinstance(value, list):
#             for item in value:
#                 self.children.append(ComposeNode(None, item))  # No key for list items

# def create_ast(key, value):
#     return ComposeNode(key, value)

def preprocess_yaml(file_content):
    # Replace {{variable}} with a placeholder token
    processed_content = file_content.replace('{{-', '#').replace('{{', ' ').replace('}}', '').replace('****', '#').replace('****', '#').replace("{%-", "#").replace("{%", "#")
    # processed_content = file_content.replace('****', '#').replace('****', '#')
    return processed_content

def postprocess_data(data):
    # Reverse the replacement after parsing
    if isinstance(data, dict):
        return {k: postprocess_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [postprocess_data(element) for element in data]
    elif isinstance(data, str):
        return data.replace('__', '{{}}')
    else:
        return data


def parse_yaml_to_ast(filename):
    with open(filename, 'r') as file:
        file_content = file.read()
        # Load YAML content
        processed_content = preprocess_yaml(file_content)
        yaml_content = yaml.safe_load(processed_content)
        
        # Initialize AST
        ast = create_ast(yaml_content)
        postprocess_data(yaml_content)
        
    return ast

def create_ast(node):
    # If the node is a dictionary, iterate through its keys
    if isinstance(node, dict):
        ast_node = {}
        for key, value in node.items():
            # Recursively process each item
            # print("key-val", key, value)
            ast_node[key] = create_ast(value)
        return ast_node
    
    # If the node is a list, process each element in the list
    elif isinstance(node, list):
        return [create_ast(item) for item in node]
    
    #TODO: Think later
    # elif isinstance(node, str):
    #     if "=" in node:
    #         ast_node = {}
    #         key_equal, valu_equal = node.split("=")
    #         # print("key_equal",key_equal)
    #         # print("valu_equal",valu_equal)
    #         # return [create_ast(item) for item in node_arr]
    #         ast_node[key_equal] = create_ast(valu_equal)
    #         return ast_node
    #     else:
    #         return node
    
    # If the node is a terminal (leaf node), simply return its value
    else:   
        return node

# # Example usage
# if __name__ == "__main__":
#     compose_file = 'compose_temp.yml'  # Specify the path to your Docker Compose file
#     ast = parse_yaml_to_ast(compose_file)
#     pprint(ast)
