# def check_missing_configurations(ast, required_configurations, alerts):
#     """Checks for missing configurations in the AST."""
#     if isinstance(ast, dict):
#         for key, required_subnode in required_configurations.items():
#             # if key is '' and ast[key] != None:
#             if key in ast:
#                 check_missing_configurations(ast[key], required_subnode, alerts)
#             else:
#                 alerts.append(f"Missing configuration: {key} should be specified for better security practices.")
#     elif isinstance(ast, list):
#         for item in ast:
#             check_missing_configurations(item, required_configurations, alerts)


# def check_missing_configurations(ast, required_configurations, alerts, path=''):
#     if isinstance(ast, dict):
#         for pattern in required_configurations:
#             for key, ast_subnode in ast.items():
#                 if key in pattern and check_ast_match(ast_subnode, pattern[key]):
#                     alerts.append(f"Antipattern found in {key}: {compose_error_descriptions[pattern['errorNo']]}")
#             check_missing_configurations(ast_subnode, required_configurations, alerts)
#     elif isinstance(ast, list):
#         for item in ast:
#             check_missing_configurations(item, required_configurations, alerts)


# def check_missing_configurations(ast, required_configurations, alerts, path=''):
#     """Checks for missing configurations in the AST using a list of configuration rules."""
#     if isinstance(ast, dict):
#         for config in required_configurations:
#             # For each configuration rule in the list, extract the path and expected structure
#             for config_path, config_values in config.items():
#                 if config_path != 'errorNo':  # Skip the error number key
#                     current_path = path + '.' + config_path if path else config_path
#                     if config_path in ast:
#                         # Recursively check this part of the AST against the configuration rule
#                         check_missing_configurations(ast[config_path], [config_values], alerts, current_path)
#                     else:
#                         # Configuration path missing in the AST
#                         error_no = config.get('errorNo', 'Unknown error number')
#                         alerts.append(f"Missing configuration at {current_path}: (Error {error_no})")
#     elif isinstance(ast, list):
#         for item in ast:
#             # Apply the same checks to each item in the list
#             check_missing_configurations(item, required_configurations, alerts, path)


# def check_missing_configurations(ast, required_configurations, alerts, path=''):
#     """Checks for missing configurations in the AST."""
#     if isinstance(ast, dict):
#         if 'services' in required_configurations and path == 'services':
#             # If we are in the 'services' section, apply the checks to each service
#             for service_name, service_config in ast.items():
#                 check_missing_configurations(service_config, required_configurations['services'], alerts, path='services')
#         else:
#             for key, required_subnode in required_configurations.items():
#                 if key in ast:
#                     # Append the current path for more specific error messages
#                     new_path = f"{path}.{key}" if path else key
#                     check_missing_configurations(ast[key], required_subnode, alerts, new_path)
#                 else:
#                     # Missing key at this level
#                     alerts.append(f"Missing configuration at {path}: {compose_error_descriptions[pattern['errorNo']]}")
#     elif isinstance(ast, list):
#         for item in ast:
#             check_missing_configurations(item, required_configurations, alerts, path)


import re


# def check_missing_configurations(ast, required_configurations, alerts,compose_error_descriptions):
#     """Checks for missing configurations in the AST."""
#     if isinstance(ast, dict):
#         for config in required_configurations:
#             config_details = config.get('services', {}).get('service', {})
#             error_no = config.get('errorNo', 'Unknown error number')
#             severity = config.get('severity', 'Unknown severity number')
#             is_value_expected: bool = config.get('expectedValue', 'Unknown expected value boolean')

#             if 'services' in ast:
#                 for service_name, service_config in ast.items():
#                     # print(config_details.items())
#                     for key, expected_value in config_details.items():
#                         # if(len(expected_value)> 1):
#                         #     print(expected_value)
#                         #     for i in range(len(expected_value)):
#                         #         check_missing_configurations(expected_value[i], required_configurations, alerts, compose_error_descriptions)

#                         print(key, expected_value)
#                         # print(service_config)
#                         if key not in service_config:
#                             # or service_config[key] in range(expected_value)
#                             # print(key)
                            
#                             alerts.append([f"Missing or incorrect configuration in service '{service_name}' : {compose_error_descriptions[str(error_no)]}",severity])
#                         elif is_value_expected and expected_value not in service_config[key]:
#                             # FIXME: This solution is only valid for volumes.
#                             for volume in service_config[key]:
#                                 # print(volume)
#                                 if not re.search(expected_value, volume):
#                                     alerts.append([f"Missing or incorrect configuration in service '{service_name}' : {compose_error_descriptions[str(error_no)]}",severity])
#                         # else:
#                         #     print(key)
                            
                            
#     elif isinstance(ast, list):
#         for item in ast:
#             check_missing_configurations(item, required_configurations, alerts)


# Check missing configurations function
def check_missing_configurations(ast, required_configurations, alerts, compose_error_descriptions):
    """Checks for missing configurations in the AST."""
    if isinstance(ast, dict):
        for config in required_configurations:
            config_details = config.get('path', {}).get('services', {}).get('service', {})
            error_no = config.get('errorNo', 'Unknown error number')
            severity = config.get('severity', 'Unknown severity number')
            is_value_expected = config.get('expectedValue', False)
            # print(ast.items())

            for service_name, service_config in ast.get('services', {}).items():
                for key, expected_value in config_details.items():
                    if key not in service_config:
                        alerts.append([f"Missing or incorrect configuration in service '{service_name}': {compose_error_descriptions[str(error_no)]}", severity])
                    elif is_value_expected and isinstance(expected_value, str):
                        if not re.search(expected_value, str(service_config.get(key, ''))):
                            alerts.append([f"Missing or incorrect configuration in service '{service_name}': {compose_error_descriptions[str(error_no)]}", severity])
                    elif isinstance(expected_value, dict):
                        for subkey, subvalue in expected_value.items():
                            if subkey not in service_config[key] or service_config[key][subkey] != subvalue:
                                alerts.append([f"Missing or incorrect configuration in service '{service_name}': {compose_error_descriptions[str(error_no)]}", severity])

    elif isinstance(ast, list):
        for item in ast:
            check_missing_configurations(item, required_configurations, alerts, compose_error_descriptions)

# def navigate_and_check(service_config, path):
#     """ Recursively navigate and check according to the nested dictionary path. """
#     if isinstance(path, dict):
#         for key, sub_path in path.items():
#             print(key, service_config)
#             if key in service_config:
#                 return navigate_and_check(service_config[key], sub_path)
#             else:
#                 return None, []  # Key not found, return empty list for expected values
#     elif isinstance(path, list):
#         return service_config, path  # Return current config and the list of expected values

#     return None, []  # Default case, if path handling does not match any expected type

# def check_missing_configurations(ast, configurations,compose_error_descriptions):
#     alerts = []
#     for config in configurations:
#         path_dict = config['path']
#         error_no = str(config['errorNo'])
#         severity = config['severity']

#         for service_name, service_config in ast.items():
#             result, expected_values = navigate_and_check(service_config, path_dict)
#             print(result)
#             if result is None or not expected_values:  # Check if there's no result or no expected values
#                 alerts.append((f"Missing or incorrect configuration in '{service_name}'", severity))
#             else:
#                 for expected in expected_values:
#                     if ':' in expected:  # Ensure the format is key:value
#                         key, value = expected.split(':')
#                         if key not in result or str(result[key]) != value:
#                             alerts.append((f"Configuration mismatch at '{key}' in '{service_name}': expected {value}", severity))
#                     else:
#                         if expected not in result:
#                             alerts.append((f"Missing key '{expected}' in '{service_name}'", severity))

#     return alerts