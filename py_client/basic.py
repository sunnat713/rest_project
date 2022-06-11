import requests

# endpoint = 'https://httpbin.org/status/200'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'
get_response = requests.post(endpoint, json={'title': 'ABC123', 'content': 'Hello world', 'price':'abs654'})
# print(get_response.text)
print(get_response.json())
