import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Function to get the GitHub API token from the environment
def get_github_token():
    return os.getenv('GITHUB_TOKEN')

def check_rate_limit(token):
    url = "https://api.github.com/rate_limit"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    rate_limit_info = response.json()

    # Output the rate limit status
    print("Rate Limit Status:")
    print(f"Core Limit: {rate_limit_info['rate']['limit']}")
    print(f"Core Remaining: {rate_limit_info['rate']['remaining']}")
    print(f"Core Resets at: {rate_limit_info['rate']['reset']} (UTC epoch seconds)")
    print(f"Search Limit: {rate_limit_info['resources']['search']['limit']}")
    print(f"Search Remaining: {rate_limit_info['resources']['search']['remaining']}")
    print(f"Search Resets at: {rate_limit_info['resources']['search']['reset']} (UTC epoch seconds)")

if __name__ == '__main__':
    # Your GitHub token
    github_token = get_github_token()
    check_rate_limit(github_token)
