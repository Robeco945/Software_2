import requests
from key import key
name = input('enter city name: ')
request = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={key}&units=metric"
response = requests.get(request).json()
print(f'weather condition: {response["weather"][0]["description"]}')
print(f'current temperature: {response["main"]["temp"]} celsius')