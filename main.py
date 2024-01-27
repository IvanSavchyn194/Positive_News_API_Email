import requests
from send_email import send_email

api_key = "d04b1d908bc54b6f804cfafd54dd00df"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-27&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""

# Access to article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        body = body + f"{article['title']}\n{article['description']}\n\n"

body = body.encode("UTF-8")
send_email(body)
