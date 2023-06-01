import pytest
import json
from unittest.mock import patch, Mock
import bravecli as bs  # assuming your code is in a file called bravecli.py

def test_get_api_key(monkeypatch):
    monkeypatch.setenv('BRAVE_API_KEY', 'test_key')
    assert bs.get_api_key() == 'test_key'
    monkeypatch.delenv('BRAVE_API_KEY')
    with patch('builtins.input', return_value='user_input_key'):
        assert bs.get_api_key() == 'user_input_key'

@patch('bravecli.requests.get')
def test_brave_web_search(mock_get):
    # Mock the JSON response from the API
    mock_response = Mock()
    mock_response.json.return_value = {
        'web': {
            'results': [
                {
                    'title': 'Test Title',
                    'description': 'Test Description',
                    'url': 'http://example.com',
                },
            ],
        },
    }
    mock_get.return_value = mock_response

    # Call the function with the query 'test_query'
    bs.brave_web_search('test_query', 'moderate')

    # Assert that the GET request was called with the correct parameters
    mock_get.assert_called_once_with(
        bs.BASE_URL, 
        headers=bs.HEADERS, 
        params={'q': 'test_query', 'safesearch': 'moderate'}
    )

def test_save_to_file(tmp_path):
    data = {'key': 'value'}
    file = tmp_path / 'test.json'
    bs.save_to_file(file, data)
    with open(file, 'r') as f:
        assert json.load(f) == data

def test_list_keys(capsys):
    results = [
        {
            'title': 'Test Title',
            'description': 'Test Description',
            'url': 'http://example.com',
        },
    ]
    bs.list_keys(results)
    captured = capsys.readouterr()
    assert captured.out == (
        'Title: Test Title\n'
        'Description: Test Description\n'
        'URL: http://example.com\n'
        '\n'
    )
