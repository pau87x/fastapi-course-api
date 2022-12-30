import requests

URL = 'http://localhost:8000/api/v1/users/reviews'
HEADERS = { 'accept': 'application/json' }

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print('Peticion exitosa')

    print(response.content)
    print('\n')

    print(response.headers)