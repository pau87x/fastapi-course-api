import requests

URL = 'http://localhost:8000/api/v1/reviews?page=1&limit=2'
HEADERS = { 'accept': 'application/json' }

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    print('Peticion exitosa')

    if response.headers.get('content-type') == 'application/json':
        reviews = response.json()

        for review in reviews:
            print(f"score: {review['score']} - {review['review']}" )