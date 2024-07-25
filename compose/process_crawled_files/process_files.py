import os

def comment_sections_with_stars(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_star_section = False
    commented_lines = []

    for line in lines:
        if line.strip().startswith('****') and line.strip().endswith('****'):
            in_star_section = not in_star_section
            commented_lines.append('# ' + line)  # Comment the toggle line
            continue

        if in_star_section:
            commented_lines.append('# ' + line)
        else:
            commented_lines.append(line)

    # Write the processed content back to the same file
    with open(file_path, 'w') as file:
        file.writelines(commented_lines)

def process_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # print(f"Processing file: {file_path}")
            comment_sections_with_stars(file_path)


def file_contains_services(file_path):
    """ Check if a file contains the word 'version' """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if 'services' in line:
                    return True
    except Exception as e:
        # print(f"Error reading {file_path}: {e}")
        raise
    return False

def check_files_in_directory(directory_path):
    """ Process each file in the directory to check for 'version' """
    files_without_services = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Ensure it's a file and not a directory
        if os.path.isfile(file_path):
            # Check if the file contains 'services'
            if not file_contains_services(file_path):
                files_without_services.append(filename)
                os.remove(file_path)

    # Output the results
    if files_without_services:
        # print("Files without 'version':")
        counter = 0
        for file in files_without_services:
            # print(file, counter)
            counter += 1
    else:
        print("All files contain 'services'.")

# Example usage
# check_files_in_directory('../../composefiles_datastore/')



process_directory('../../composefiles_datastore/')
