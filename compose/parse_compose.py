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

def parse_yaml_to_ast(filename):
    with open(filename, 'r') as file:
        # Load YAML content
        yaml_content = yaml.safe_load(file)
        
        # Initialize AST
        ast = create_ast(yaml_content)
        
    return ast

def create_ast(node):
    # If the node is a dictionary, iterate through its keys
    if isinstance(node, dict):
        ast_node = {}
        for key, value in node.items():
            # Recursively process each item
            ast_node[key] = create_ast(value)
        return ast_node
    
    # If the node is a list, process each element in the list
    elif isinstance(node, list):
        return [create_ast(item) for item in node]
    
    # If the node is a terminal (leaf node), simply return its value
    else:
        return node

# # Example usage
# if __name__ == "__main__":
#     compose_file = 'compose_temp.yml'  # Specify the path to your Docker Compose file
#     ast = parse_yaml_to_ast(compose_file)
#     pprint(ast)
