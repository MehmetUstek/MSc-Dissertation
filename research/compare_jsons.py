
import json

# Function to load JSON from a file
def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

# Function to convert lists in JSON data to sets
def convert_lists_to_sets(json_data):
    for key in json_data:
        json_data[key] = set(json_data[key])
    return json_data


ground_truth_terraform_filepath = './ground_truth/ground_truth_terraform_data.json'
generated_truth_terraform_filepath = './generated_truth/generated_truth_terraform_data.json'

ground_truth_dockerfile_filepath = './ground_truth/ground_truth_dockerfile_data.json'
generated_truth_dockerfile_filepath = './generated_truth/generated_truth_dockerfile_data.json'

ground_truth_compose_filepath = './ground_truth/ground_truth_compose_data.json'
generated_truth_compose_filepath = './generated_truth/generated_truth_compose_data.json'


# Load JSON files
json1 = load_json(ground_truth_terraform_filepath)
json2 = load_json(generated_truth_terraform_filepath)

json3 = load_json(ground_truth_dockerfile_filepath)
json4 = load_json(generated_truth_dockerfile_filepath)

json5 = load_json(ground_truth_compose_filepath)
json6 = load_json(generated_truth_compose_filepath)


# Convert lists to sets
json1_sets = convert_lists_to_sets(json1)
json2_sets = convert_lists_to_sets(json2)

json3_sets = convert_lists_to_sets(json3)
json4_sets = convert_lists_to_sets(json4)

json5_sets = convert_lists_to_sets(json5)
json6_sets = convert_lists_to_sets(json6)


def calculate_similarity(json1_sets, json2_sets, file_type):
    # Calculate similarity
    total_similarity = 0
    common_keys = json1_sets.keys() & json2_sets.keys()  # Intersect keys
    for key in common_keys:
        intersection = len(json1_sets[key] & json2_sets[key])
        union = len(json1_sets[key] | json2_sets[key])
        if union > 0:
            total_similarity += (intersection / union)

    # Compute overall similarity percentage
    if common_keys:
        overall_similarity = (total_similarity / len(common_keys)) * 100
        print(f"The {file_type} files are {overall_similarity:.2f}% similar")
    else:
        print("No common keys to compare.")

calculate_similarity(json1_sets, json2_sets, "Terraform")
calculate_similarity(json3_sets, json4_sets, "Compose")
calculate_similarity(json5_sets, json6_sets, "Dockerfile")
