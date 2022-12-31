import requests

REVIEW_ID = 25
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.delete(URL)

if response.status_code == 200:
    print('Review elimnada')

    print(response.json()['id'])
else:
    print( response.content )