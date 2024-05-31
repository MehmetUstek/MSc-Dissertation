import yaml

def parse_yaml_to_ast(filename):
    with open(filename, 'r') as file:
        # Load YAML content
        yaml_content = yaml.safe_load(file)

    # Initialize AST by calling create_ast with the full YAML content
    return create_ast(yaml_content, generalize_services=True)

def create_ast(node, generalize_services=False):
    # Handle dictionary types possibly containing services or other configurations
    if isinstance(node, dict):
        ast_node = {}
        if 'services' in node and generalize_services:
            # Special handling for services to anonymize service names
            service_ast = {}
            for idx, (service_name, service_details) in enumerate(node['services'].items()):
                # Assign a generic name to each service
                generic_service_name = f"service_{idx}"
                service_ast[generic_service_name] = create_ast(service_details)
            ast_node['services'] = service_ast
        else:
            # Regular processing for other keys
            for key, value in node.items():
                ast_node[key] = create_ast(value)
        return ast_node

    # Handle list types which could be part of any configuration
    elif isinstance(node, list):
        return [create_ast(item) for item in node]

    # Base case: return the node as is for simple types
    else:
        return node

# Example usage of the parser
ast = parse_yaml_to_ast('compose_temp.yml')
print(ast)
