import requests
name = input('enter city name: ')
request = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid=36f80f5b6457341641e2b73c4abe0e19&units=metric"
response = requests.get(request).json()
print(f'weather condition: {response["weather"][0]["description"]}')
print(f'current temperature: {response["main"]["temp"]} celsius')