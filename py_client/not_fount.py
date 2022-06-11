import requests

endpoint = 'http://localhost:8000/api/product/102/'
data = {
    'title':'Nima gap',
    # 'content':'Tinchmi',
    'price':212.12
}
get_response = requests.get(endpoint)
print(get_response.json())
