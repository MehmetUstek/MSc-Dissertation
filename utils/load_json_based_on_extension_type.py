from utils import load_json
from utils.extension_enum import Extension


def load_json_based_on_extension_type(extension):

    if extension == Extension.Dockerfile:
        return load_json('dockerfileVulnerability/antipattern_descriptions.json')
    elif extension == Extension.Compose:
        return load_json('compose/antipattern_descriptions.json')
    elif extension == Extension.Terraform:
        return load_json('terraform/antipattern_descriptions.json')
    
def load_consequences_based_on_extension_type(extension):

    if extension == Extension.Dockerfile:
        return load_json('dockerfileVulnerability/consequences.json')
    elif extension == Extension.Compose:
        return load_json('compose/consequences.json')
    elif extension == Extension.Terraform:
        return load_json('terraform/consequences.json')
    
def load_explanations_based_on_extension_type(extension):

    if extension == Extension.Dockerfile:
        return load_json('dockerfileVulnerability/explanations.json')
    elif extension == Extension.Compose:
        return load_json('compose/explanations.json')
    elif extension == Extension.Terraform:
        return load_json('terraform/explanations.json')