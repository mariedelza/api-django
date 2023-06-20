import requests

id=input('entrez id du produit a supprimer:')
endpoint=f"http://127.0.0.1:8000/product/{id}/delete"
response=requests.delete(endpoint)
print(response.status_code,response.status_code==204)