import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Top business headlines in the US right now from newsapi.org
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

# Get the data from the URL and jsonify it
content = requests.get(url).json()

for news in content['articles']:
	info = f"""
Title: {news['title'].split(" - ")[0]}
Author: {news['author']}
{f"Description: {news['description']}" if news['description'] else "No description :("}
URL: {news['url']}
"""
	print(info)
	print(" ------------------------------------ ")

