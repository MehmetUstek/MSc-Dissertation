import json

import hcl2


def transform_resources(resources):
    transformed = []
    for resource in resources:
        for resource_type, resource_details in resource.items():
            for resource_name, resource_config in resource_details.items():
                transformed.append({
                    resource_type: {
                        "resource_name": resource_name,
                        "resource_configuration": resource_config
                    }
                })
    return transformed

def parse_terraform(hcl_file_path):
    with open(hcl_file_path, 'r') as file:
        hcl_content = file.read()
    
    return helper_function(hcl_content)


def parse_terraform_from_file_content(file_content):
    return helper_function(file_content)

    

def helper_function(hcl_content):
    # Parse HCL content
    hcl_dict = hcl2.loads(hcl_content)
    
    # Initialize final JSON structure
    final_structure = {}
    
    # Handle providers
    # if 'provider' in hcl_dict:
    #     final_structure['provider'] = hcl_dict['provider']
    for key in hcl_dict:
        if key !="resource":
            final_structure[key] = hcl_dict[key]
    
    # Transform resources
    if 'resource' in hcl_dict:
        final_structure['resource'] = transform_resources(hcl_dict['resource'])
    
    # Convert the parsed and transformed HCL to JSON
    with open( 'output.json', 'w') as json_file:
        json.dump(final_structure, json_file, indent=4)
    return final_structure

# Example usage
# parse_terraform('example.tf')
