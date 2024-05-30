import re

def check_password_plaintext(password):
    """
    Check the format of a given password string.
    
    Args:
    password (str): The password string to check.
    
    Returns:
    str: Description of the password format.
    """
    # Regex to match template-like patterns e.g., {{ var_name }}
    template_pattern = r"\{\{\s*[\w_]+\s*\}\}"
    
    # Check if the password matches the template pattern
    if re.match(template_pattern, password):
        return False
    else:
        return True

# Example usage:
# passwords = [
#     "{{ mysql_root_password }}",
#     "simplepassword123",
#     "{{user_pass}}"
# ]

# for pwd in passwords:
#     print(f"Password: {pwd} - {check_password_plaintext(pwd)}")
