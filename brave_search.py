import argparse
import json
import os
import requests
import sys


YOUR_API_KEY = os.environ.get('BRAVE_API_KEY')

HEADERS = {
    'Accept': 'application/json',
    'X-Subscription-Token': YOUR_API_KEY,
}

def brave_web_search(query):
    url = 'https://api.search.brave.com/res/v1/web/search'
    params = {'q': query}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def brave_suggest_search(query, country='US', count=5):
    url = 'https://api.search.brave.com/res/v1/suggest/search'
    params = {'q': query, 'country': country, 'count': count}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def brave_spell_check_search(query, country='US'):
    url = 'https://api.search.brave.com/res/v1/spellcheck/search'
    params = {'q': query, 'country': country}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()
def save_to_file(result, file_path):
    with open(file_path, 'w') as f:
        json.dump(result, f, indent=4)
def brave_web_search(query):
    url = 'https://api.search.brave.com/res/v1/web/search'
    params = {'q': query}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def list_results(results):
    for result in results['web']['results']:
        print(f'Title: {result["title"]}')
        print(f'Description: {result["description"]}')
        print(f'URL: {result["url"]}')
        print('---')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help="can be one of 'web_search', 'suggest_search', 'spell_check_search'")
    parser.add_argument('query', help='the search query')
    parser.add_argument('-s', '--save', help='file path to save the result')
    parser.add_argument('-l', '--list', action='store_true', help='list only title, description, and url for web_search')
    args = parser.parse_args()

    if args.command == 'web_search':
        result = brave_web_search(args.query)
        if args.list:
            list_results(result)
        else:
            print(result)
    elif args.command == 'suggest_search':
        result = brave_suggest_search(args.query)
        print(result)
    elif args.command == 'spell_check_search':
        result = brave_spell_check_search(args.query)
        print(result)
    else:
        print('Invalid command. Use web_search, suggest_search, or spell_check_search.')
        return

    if args.save:
        save_to_file(result, args.save)

if __name__ == "__main__":
    main()
