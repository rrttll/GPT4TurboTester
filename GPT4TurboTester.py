import requests
import json
import os

def query_openai():
    api_key = os.environ.get('OPENAI_API_KEY') # add variable each session
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
    'model': 'gpt-4-1106-preview',  # Adjust model name if necessary
    'messages': [
        {'role': 'system', 'content': 'You are an assistant.'},
        {'role': 'user', 'content': 'I still have the same import request error'}
    ]
}
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()

response = query_openai()
print(response)
