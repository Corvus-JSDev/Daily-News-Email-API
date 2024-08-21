import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Top business headlines in the US right now from newsapi.org
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

get = requests.get(url)
content = get.json()
# print(content)
# print(f"totalResults: {content['articles']}")
article = content['articles'][0]

info = f"""
Title: {article['title']}
Author: {article['author']}
{f"Description: {article['description']}" if article['description'] else "No description :("}
URL: {article['url']}
"""

print(info)

