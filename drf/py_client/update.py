import requests

endpoint = "http://localhost:8000/api/products/1/update/"       #"http://127.0.0.1:8000/"

data ={
    "title": "This title is updated",
    "price" : 17.95
}
get_response = requests.put(endpoint, json = data)        # HTTP REQUEST to get endpoint
print(get_response.json()) 
