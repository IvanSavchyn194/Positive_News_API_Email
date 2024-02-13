import os
import requests
from nltk.sentiment import SentimentIntensityAnalyzer
from send_email import send_email

analyzer = SentimentIntensityAnalyzer()

API_KEY = os.getenv("newsapi_API_KEY")
topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&language=en&sortBy=publishedAt&apiKey={API_KEY}"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = f"Subject: Today's positive news about {topic}\n"

# Access to article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        positivity = analyzer.polarity_scores(article['description'])
        if positivity["compound"] > 0:
            body = body + f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

body = body.encode("UTF-8")
send_email(body)
