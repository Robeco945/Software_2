import requests

keyword = input('enter keyword: ')

request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response[0]['show']['name'])