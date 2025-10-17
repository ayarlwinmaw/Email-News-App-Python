import requests
import os
from dotenv import load_dotenv
from send_email import send_email

# Load API key from env
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

topic = "AI"

# URL for newsapi
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       # f"from=2025-09-16&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}&"
       f"language=en")

# Make request
request = requests.get(url)

# Get a dictionary of articles
content = request.json()

# print(content["articles"]) # Breakpoint to inspect the json data

# Access the article titles and description
body = f""


for article in content["articles"][:20]:
    title = article.get("title")
    description = article.get("description")
    article_url = article.get("url")

    if title and description:
        body += (f"<p><strong>{title}</p></strong>"
                 f"<p>{description}</p>"
                 f"<p>{article_url}</p>"
                 f"<p></p>")

# body = body.encode("utf8")
# send_email(message=body)
# print(body)

html_body = f"""
<html>
  <body>
    <h2><strong>Here are update news about {topic}!</strong></h2>
    {body}
  </body>
</html>
"""

message = (f"Subject:{topic} News Digest\n"
           f"Content-Type: text/html\n\n"
           f"{html_body}")
send_email(message=message.encode("utf8"))
