import os
import argparse
import requests
import json
from dotenv import load_dotenv
from typing import Dict

# Load environment variables from .env file
load_dotenv()

def get_api_key() -> str:
    api_key = os.getenv('BRAVE_API_KEY')
    if api_key is None:
        print("No API key found. You can get your API key at \n  Signup https://api.search.brave.com/ \n  Get API KEY https://api.search.brave.com/app/keys ")
        print("Please enter your Brave API key: ", end="")
        api_key = input('Please enter your Brave API key: ')
        with open('.env', 'w') as f:
            f.write(f"BRAVE_API_KEY={api_key}")
        print("API Key Saved to .env")
    return api_key



BASE_URL = 'https://api.search.brave.com/res/v1/web/search'
HEADERS = {
    "Accept": "application/json",
    "X-Subscription-Token": get_api_key()
}

def save_to_file(filename: str, data: Dict):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def list_keys(results):
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Description: {result['description']}")
        print(f"URL: {result['url']}")
        print()

def brave_web_search(query: str, safesearch: str, list_only: bool = False, save: str = None):
    response = requests.get(
        BASE_URL, 
        headers=HEADERS, 
        params={'q': query, 'safesearch': safesearch}
    )
    
    data = response.json()
    if data.get('type') == 'ErrorResponse':
        print("Error Please check An error occurred while fetching the data. \n Please check your API key and search parameters.")
        print(f"BRAVE_API_KEY={os.getenv('BRAVE_API_KEY')}")
        return -1
    results = data.get('web', {}).get('results', [])
    if list_only:
        list_keys(results)
    elif save:
        save_to_file(save, data)
    else:
        print(json.dumps(data, indent=4))

def main():
    parser = argparse.ArgumentParser(description="Search the web with Brave's API.")
    parser.add_argument("command", help="Command to run. Currently only 'web_search' is supported.")
    parser.add_argument("query", help="Search query.")
    parser.add_argument("--safesearchoff", action='store_true', help="Turn off safe search.")
    parser.add_argument("-s", "--save", help="Save results to file.")
    parser.add_argument("-l", "--list", action='store_true', help="Only list 'title', 'description' and 'url' from results.")
    args = parser.parse_args()

    safesearch = "off" if args.safesearchoff else "moderate"

    if args.command == "web_search":
        brave_web_search(args.query, safesearch, args.list, args.save)
    else:
        print(f"Unknown command: {args.command}")
        print("Usage: python bravecli.py web_search 'query' [--safesearchoff] [-s savefile.json] [-l]")

if __name__ == "__main__":
    main()
