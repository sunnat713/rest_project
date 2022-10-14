import requests

endpoint = 'http://192.168.28.114:9999/api/product/'
headers = {'Authorization': 'Token 47bc0ed1f77ef335d11c1342d72d703d1b7528bf'}
get_response = requests.get(endpoint, headers=headers)

print(get_response.json())