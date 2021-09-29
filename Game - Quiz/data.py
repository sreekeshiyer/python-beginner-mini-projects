import requests

url = 'https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean'

response = requests.get(url=url)

data = response.json()['results']

question_data = data
