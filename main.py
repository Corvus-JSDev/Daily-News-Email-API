import requests

url = "https://finance.yahoo.com/"

get = requests.get(url)
content = get.text
print(content)
