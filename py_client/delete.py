import requests

product_id = input('product id kiriting\n')

try:
    product_id = int(product_id)
except:

    print(f'{product_id} validatsiyadan otmadi son kiriting')
    product_id = None
if product_id:
    endpoint = f'http://localhost:8000/api/product/{product_id}/delete/'
    data = {
        'title': 'Test22',
        'content': 'Test33',
        'price': 1245
    }
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204 )
