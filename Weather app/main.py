import requests


"""
Register yourself in https://openweathermap.org/ and create an account then go to this page: https://home.openweathermap.org/api_keys. Then generate a key
"""
# paste your api key here
api_key = "YOUR_API_KEY_HERE"

# getting city name from user
city = input("Enter city name: ")

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
)

# getting the data
print(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
print(f"Temperature: {data.json().get('main')['temp']}°C")
print(f"Weather: {data.json().get('weather')[0].get('main')}")
print(f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C")
print(f"Humidity: {data.json().get('main')['humidity']}%")
print(f"Wind: {data.json().get('wind')['speed']} km/h")