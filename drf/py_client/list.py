import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"       #"http://127.0.0.1:8000/"

username = input("What is your username? \n")
password = getpass("What is your password? \n")

auth_response = requests.post(auth_endpoint, json={'username': username , 'password': password})        # HTTP REQUEST to get endpoint
print(auth_response.json()) 

if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    headers = {
        "Authorization": f"Token {token}"
    }

    endpoint = "http://localhost:8000/api/products/"       #"http://127.0.0.1:8000/"

    get_response = requests.get(endpoint, headers=headers)        # HTTP REQUEST to get endpoint
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print("next_url", next_url) 
    print(results)
    # if next_url is not None:
    #     get_response = requests.get(next_url, headers=headers)
# else:
#     print("Authentication failed!")
     