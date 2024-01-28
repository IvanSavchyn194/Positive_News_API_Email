import requests
from send_email import send_email

topic = "tesla"

api_key = "d04b1d908bc54b6f804cfafd54dd00df"
url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = "Subject: Today's news\n"

# Access to article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

body = body.encode("UTF-8")
send_email(body)
