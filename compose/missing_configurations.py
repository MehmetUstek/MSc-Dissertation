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


def check_missing_configurations(ast, required_configurations, alerts,compose_error_descriptions):
    """Checks for missing configurations in the AST."""
    if isinstance(ast, dict):
        for config in required_configurations:
            config_details = config.get('services', {}).get('service', {})
            error_no = config.get('errorNo', 'Unknown error number')

            if 'services' in ast:
                for service_name, service_config in ast['services'].items():
                    for key, expected_value in config_details.items():
                        if key not in service_config :
                            # or service_config[key] in range(expected_value)
                            alerts.append([f"Missing or incorrect configuration in service '{service_name}' : {compose_error_descriptions[str(error_no)]}",5])
    elif isinstance(ast, list):
        for item in ast:
            check_missing_configurations(item, required_configurations, alerts)
