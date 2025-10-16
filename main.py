import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load API key from env
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

# URL for newsapi
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-09-16&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary of articles
content = request.json()

# print(content["articles"])

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf8")
send_email(message=body)