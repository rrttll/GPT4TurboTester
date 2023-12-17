import requests
import os

def query_openai(prompt):
    api_key = os.environ.get('OPENAI_API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4-1106-preview',  # Adjust the model as needed
        'messages': [{"role": "system", "content": "You are a helpful assistant."}, 
                     {"role": "user", "content": prompt}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()

def main():
    print("GPT-4 Turbo Chat (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        response = query_openai(user_input)
        ai_response = response['choices'][0]['message']['content']
        print("AI:", ai_response)

if __name__ == "__main__":
    main()
