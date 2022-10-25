import requests
import json


def read_news(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


api_key = ''  # your api key

url = (
    f'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={api_key}')

res = requests.get(url).json()
# print(res['articles'][1]['title'])
read_news("Welcome to xyz news...")
for i in range(len(res)):
    news = f"News number {i + 1}. Title: {res['articles'][i]['title']}. Description:{res['articles'][i]['description']}"
    if i > 0:
        read_news("Moving towards the next news")
    read_news(news)
