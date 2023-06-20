import requests

endpoint="http://127.0.0.1:8000/product/create-list/"
response=requests.post(endpoint,json={'name':'orange','content':'','price':200})
print(response.json())
print(response.status_code)