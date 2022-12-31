import requests

URL = 'http://localhost:8000/api/v1/reviews'
REVIEW = {
  "user_id": 2,
  "movie_id": 6,
  "review": "Esta chida! Enviada desde el cliente",
  "score": 5
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Review creada')

    print(response.json()['id'])
else:
    print( response.content )