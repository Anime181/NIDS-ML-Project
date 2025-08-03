
import requests

def get_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    response = requests.post(url, data={
        "apikey": api_key,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    })
    return response.json()["access_token"]

def score_model(token, deployment_url, fields, values):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    payload = {
        "input_data": [
            {
                "fields": fields,
                "values": values
            }
        ]
    }
    response = requests.post(deployment_url, json=payload, headers=headers)
    return response.json()
