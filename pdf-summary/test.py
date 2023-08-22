import requests
import json


# get Seaplane access token
def get_token(api_key):
    url = "https://flightdeck.cplane.cloud/identity/token"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.post(url, headers=headers)
    return response


# construct data component with PDF link
data = data = {"input": [{"url": "https://arxiv.org/pdf/2102.07350.pdf"}]}

# convert to json
json_data = json.dumps(data)

# get the token
response = get_token("<YOUR-SEAPLANE-API-KEY>")

# Set the token and URL
token = response.text
url = "https://carrier.staging.cplane.dev/apps/pdf-summary/latest/demo-input"

# Set the headers
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# Make the POST request
api_response = requests.post(url, headers=headers, data=json_data)

# Print the response
print(api_response.text)
