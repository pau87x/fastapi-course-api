import requests

REVIEW_ID = 25
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'
REVIEW = {
  "review": "Esta chida pero no tanto! Enviada desde el cliente.",
  "score": 2
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200:
    print('Review actualizada')

    print(response.json()['id'])
else:
    print( response.content )