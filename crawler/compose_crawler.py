import argparse
import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to get the GitHub API token from the environment
def get_github_token():
    return os.getenv('GITHUB_TOKEN')


def search_github(token, extension, exclude_names, start_page=1, items_per_page=30):
    url = "https://api.github.com/search/code"
    headers = {'Authorization': f'token {token}'}
    
    # Build the query to include the extension and exclude specific filenames
    query = f"extension:{extension}"
    include_names = ["aws"]
    for name in include_names:
        query += f" filename:{name}"
    for name in exclude_names:
        query += f" -filename:{name}"
        
    params = {
        'q': query + " in:path",
        'per_page': items_per_page,
        'page': start_page
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['items'], response.headers


def download_files(items, directory="downloaded_aws_terraform_files", last_index_file="last_index.txt"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    last_index = 0
    if os.path.exists(last_index_file):
        with open(last_index_file, 'r') as f:
            last_index = int(f.read().strip())

    for index, item in enumerate(items, start=last_index+1):
        file_url = item['html_url'].replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        file_name = f"{item['repository']['name']}-{item['name']}"
        file_path = os.path.join(directory, file_name)
        if  os.path.exists(file_path):
            print("File exists")
        else:
            # Filter out unwanted files based on naming conventions
            if any(unwanted in file_name.lower() for unwanted in ["example", "template", "_in.md", ".js"]):
                print(f"Skipping unwanted file: {file_name}")
                continue

            response = requests.get(file_url)
            if response.status_code == 200:
                with open(file_path, 'w') as file:
                    file.write(response.text)
                print(f"Downloaded {file_path}")
                with open(last_index_file, 'w') as f:
                    f.write(str(index))
            else:
                print(f"Failed to download {file_url}")

if __name__ == '__main__':
    # Your GitHub token
    github_token = get_github_token()
    if not github_token:
        print("GitHub token is not set in the environment.")
        exit()

    parser = argparse.ArgumentParser(description="AST-matching IaC configuration file vulnerability scanner", add_help=True)
    parser.add_argument('-s', '--start', type=int, help='Start index', required=True)
    
    args = parser.parse_args()
    
    # Manual start index for API pagination
    start_index = args.start  # This is the item index from which you want to start
    items_per_page = 30  # Set this according to GitHub API limits and your preference

    # Calculate start page based on the start index and items per page
    start_page = (start_index // items_per_page) + 1

    # Compose file search queries
    # compose_files = ['filename:docker-compose.yml', 'filename:docker-compose.yaml', 'filename:compose.yml', 'filename:compose.yaml']
    # file_query = 'filename:.tf'
    all_items = []

    extension = '.tf'
    exclude_names = ['output', 'variables', 'example', 'template', 'versions','auto','provider']


    # for file_query in compose_files:
    keep_searching = True
    while keep_searching:
        items, headers = search_github(github_token, extension, exclude_names, start_page=start_page, items_per_page=items_per_page)
        download_files(items)
        if 'next' in headers.get('Link', ''):
            start_page += 1
        else:
            keep_searching = False
        # Check rate limits
        if int(headers.get('X-RateLimit-Remaining', 1)) < 10:
            print("Approaching rate limit, pausing for a minute...")
            time.sleep(70)  # Sleep for one min
