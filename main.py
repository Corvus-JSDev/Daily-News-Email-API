import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Top business headlines in the US right now from newsapi.org
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

# Get the data from the URL and jsonify it
content = requests.get(url).json()
message_to_send = """"""

for news in content['articles']:
	message_to_send += f"""
<hr style="border: 1px solid black; margin: 25px 0px">

<h3>
{news['title'].split(" - ")[0]}
</h3>
<p>
Author: {news['author']}
</p>
<p>
{f"Description: {news['description']}" if news['description'] else "No description :("}
</p>
<br>
<br>
<a href="{news['url']}">
Source: {news['source']['name']}
</a>
"""

# print(message_to_send)
send_email("DailyBusinessNews@gmail.com", "Top Business News", message_to_send)
