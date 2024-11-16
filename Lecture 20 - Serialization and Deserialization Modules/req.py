import requests

laptops_url = 'https://crudcrud.com/api/efb11ff5219a47f59a15d32ffa53ed39/laptops'

response = requests.get(laptops_url).json()

print(response)

for laptop in response:
    print(laptop['_id'])


laptop = {'brand': 'Asus', 'model': "TUF"}

response = requests.post(laptops_url, json=laptop)

print(response.json())


laptops_url += '/6738675200892d03e8b4cd78'

laptop = {'brand': 'Asus', 'model': "TUF Pro"}

response = requests.put(laptops_url, json=laptop)

print(response)


response = requests.delete(laptops_url)

print(response)