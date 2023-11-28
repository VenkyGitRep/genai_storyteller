from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
app.config['WTF_CSRF_ENABLED'] = False
@app.route('/')
def index():
    return render_template('index.html')


import requests

def call_openai_api(prompt):
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    
    headers = {
        'Authorization': f'Bearer {openai_api_key}'
    }
    data = {
       # 'model': 'code-davinci-002',   Choose an appropriate model for code generation
     #   'model':'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 200  # Adjust as needed
    }
    #response = requests.post('https://api.openai.com/v1/engines/code-davinci-002/completions', headers=headers, json=data)
    #response = requests.post('https://api.openai.com/v1/engines/completions', headers=headers, json=data)
    #response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', headers=headers, json=data)
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', headers=headers, json=data)
    
     # Print the request and response details
    print("Request Headers:", headers)
    print("Request Body:", data)
    print("Response Object:", response)
    print("Response Content:", response.text)

    return response.json().get('choices', [{}])[0].get('text', '').strip()


@app.route('/generate-text', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    # Placeholder for OpenAI API call
    generated_text = call_openai_api(prompt)  # Temporary placeholder
    response = jsonify({'text_response': generated_text})
    print(response.data)  # This prints the response data
    return response

if __name__ == '__main__':
    app.run(debug=True)

