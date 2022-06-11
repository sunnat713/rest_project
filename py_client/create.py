import requests

headers = {'Authorization': 'Bearer 1715ae89a1e2832d2953845b7490dd40cd3cbc88'}

endpoint = 'http://localhost:8000/api/product/'
data = {
    'title': 'Nima gap',
    'content': 'Tinchmi221',
    'price': 212.12
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
