import requests

headers ={'Authorization': 'Token  5a95afa55ad1a32fefc92d342652c5a1d16e877f'}

endpoint = "http://localhost:8000/api/products/"       #"http://127.0.0.1:8000/"

data = {
    "title": "This is title.",
    "price": 15.89,
}
get_response = requests.get(endpoint, json= data, headers=headers )        # HTTP REQUEST to get endpoint
print(get_response.json()) 
     