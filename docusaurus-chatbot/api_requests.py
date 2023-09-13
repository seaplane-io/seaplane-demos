import requests
import json


def get_token(api_key):
    """
    Requests a Seaplane JWT token based on your API key

    Args:
        api_key (string): Your Seaplane API key

    Returns:
        string: Seaplane JWT token
    """
    url = "https://flightdeck.cplane.cloud/identity/token"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.post(url, headers=headers)
    return response


def post_request(api_key, prompt, history):
    """
    Perform a POST request to your deployed chatbot to answer a new question
    from a user

    Args:
        api_key (string): Seaplane API key prompt (string): The prompt you want
        to send to your LLM history (list): The chat history as a list of tuples
        [(q,a), (q,a),...]

    Returns:
        string: JSON object containing your request id, for more info see
        https://developers.seaplane.io/docs/apps/entry-point/http-entry-point
    """
    # construct data component with your name
    data = {
        "input": [
            {
                "query": prompt,
                "chat_history": history,
            }
        ],
        "params": {"params": "not needed at the moment"},
    }

    # convert to json
    json_data = json.dumps(data)

    # get the token
    response = get_token(api_key)

    # Set the token and URL
    token = response.text
    url = "https://carrier.cplane.cloud/apps/chat-app-seaplane-docs/latest/chat"

    # Set the headers
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Make the POST request
    api_response = requests.post(url, headers=headers, data=json_data)
    print(api_response.content)

    # return the response
    return api_response.content


def get_request(api_key, request_id):
    """
    Get the inferenced result out of Seaplane using your batch ID.

    Args:
        api_key (string): Seaplane API key request_id (string): The request ID
        provided

    Returns:
        string: A JSON string containg the result of your pipeline. For more
        info on GET request outputs see
        https://developers.seaplane.io/docs/apps/entry-point/http-entry-point#get-request
    """
    # get the token
    response = get_token(api_key)

    # Set the token and URL
    token = response.text
    url = (
        "https://carrier.cplane.cloud/apps/chat-app-seaplane-docs/latest/chat/request/"
        + request_id
    )

    # Set the headers
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    # Make the POST request
    api_response = requests.get(url, headers=headers)

    # Print the response
    return api_response.content
