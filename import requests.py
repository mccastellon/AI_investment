import requests

API_KEY = 'ff6914792e3bf5aadbddaad3e8d3735b46ac8010'

# Set the Serper API endpoint
url = 'https://google.serper.dev/search'

# Set the search query
search_query = 'real estate data'

# Set the API key as a parameter
params = {
    'q': search_query,
    'api_key': API_KEY
}

# Make the HTTP request
response = requests.get(url, params=params)

# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Process the data
    print(data)
else:
    print('Error:', response.status_code)