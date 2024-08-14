from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Serper API key
API_KEY = 'ff6914792e3bf5aadbddaad3e8d3735b46ac8010'

# Natural Language Processing (NLP) library
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Define a function to process user input
def process_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input)
    # Lemmatize the tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    # Join the lemmas into a string
    query = ' '.join(lemmas)
    return query

# Define a function to make API requests to Serper
def make_api_request(query):
    url = 'https://google.serper.dev/search'
    params = {
        'q': query,
        'api_key': API_KEY
    }
    response = requests.get(url, params=params)
    return response.json()

# Define a function to generate a response
def generate_response(data):
    response = ''
    for result in data['results']:
        response += f"**{result['title']}**\n{result['description']}\n\n"
    return response

# Define the chatbot endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']
    query = process_input(user_input)
    data = make_api_request(query)
    response = generate_response(data)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)