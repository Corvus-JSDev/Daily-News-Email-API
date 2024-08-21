import requests
import os
from dotenv import load_dotenv
from send_email import send_email

def month_converter(arg):
	match arg:
		case "01":
			return "Jan."
		case "02":
			return "Feb."
		case "03":
			return "Mar."
		case "04":
			return "Apr."
		case "05":
			return "May"
		case "06":
			return "June"
		case "07":
			return "July"
		case "08":
			return "Aug."
		case "09":
			return "Sep."
		case "10":
			return "Oct."
		case "11":
			return "Nov."
		case "12":
			return "Dec."
		case _:
			return arg


load_dotenv()
API_KEY = os.getenv("API_KEY")

# Top business headlines in the US right now from newsapi.org
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}&language=en"

# Get the data from the URL and jsonify it
content = requests.get(url).json()
message_to_send = """"""

iteration = 0
for news in content['articles']:
	iteration += 1

	if iteration <= 10:
		publish_date = news['publishedAt'].split("T")[0].split("-")[::-1]
		publish_date[1] = month_converter(publish_date[1])
		publish_date = " ".join(publish_date)

		message_to_send += f"""
<hr style="border: 1px solid black; margin: 25px 0px">

<h3>
{news['title'].split(" - ")[0]}
</h3>
<p>
By {news['author']}
</p>
<i>{publish_date}</i>
<br>
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
