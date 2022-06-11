import requests

endpoint = 'http://localhost:8000/api/product/1/update/'
data = {
    'title': 'Test22',
    'content': 'Test33',
    'price': 1245
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
