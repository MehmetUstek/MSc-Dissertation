import re

def add_antipattern(matches, error_no, severity, service_name ):
    matches.append({"errorNo":str(error_no),"severity":severity, "is_missing_configuration":True,"key":service_name})


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
                        add_antipattern(alerts, error_no, severity, service_name)
                        
                        # alerts.append([f"Missing or incorrect configuration in service '{service_name}': {compose_error_descriptions[str(error_no)]}", severity])
                    elif is_value_expected and isinstance(expected_value, str):
                        if not re.search(expected_value, str(service_config.get(key, ''))):
                            add_antipattern(alerts, error_no, severity, service_name)
                    elif isinstance(expected_value, dict):
                        for subkey, subvalue in expected_value.items():
                            if subkey not in service_config[key]:
                                add_antipattern(alerts, error_no, severity, service_name)
                            elif service_config[key][subkey] != subvalue:
                                add_antipattern(alerts, error_no, severity, service_name)



    elif isinstance(ast, list):
        for item in ast:
            check_missing_configurations(item, required_configurations, alerts, compose_error_descriptions)