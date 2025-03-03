import requests

endpoint = "http://localhost:8000/api/"       #"http://127.0.0.1:8000/"

get_response = requests.post(endpoint, json={"title": "Hello world"})        # HTTP REQUEST to get endpoint
# print(get_response.headers)
# print(get_response.text)
print(get_response.json()) 
