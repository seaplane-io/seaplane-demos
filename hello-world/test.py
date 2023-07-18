import requests
import json
import sys
import os

# get Seaplane access token
def get_token(api_key):

    url = 'https://flightdeck.cplane.cloud/identity/token'
    headers = {
        'Authorization': 'Bearer ' + api_key
    }

    response = requests.post(url, headers=headers)
    return response

def post_request(api_key, name):
    
    # construct data component with your name
    data = data = {
        'input' : [
        {'name': name}]
    }

    # convert to json
    json_data = json.dumps(data)

    # get the token
    response = get_token(api_key)

    # Set the token and URL
    token = response.text
    url = 'https://carrier.staging.cplane.dev/apps/hello-world/latest/hello'

    # Set the headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Make the POST request
    api_response = requests.post(url, headers=headers, data=json_data)

    # Print the response
    return api_response.text


def get_request(api_key, request_id):

    # get the token
    response = get_token(api_key)

    # Set the token and URL
    token = response.text
    url = 'https://carrier.staging.cplane.dev/apps/hello-world/latest/hello/request/' + request_id

    # Set the headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Make the POST request
    api_response = requests.get(url, headers=headers)

    # Print the response
    return api_response.text

# Get the API key
API_KEY = os.getenv('SEAPLANE_KEY')

# if user wants POST run post request
if sys.argv[1] == "POST":
    YOUR_NAME = sys.argv[2]
    print(post_request(API_KEY, YOUR_NAME))

# if user wants GET run get request 
elif sys.argv[1] == "GET":
    REQUEST_ID = sys.argv[2]
    print(get_request(API_KEY, REQUEST_ID))