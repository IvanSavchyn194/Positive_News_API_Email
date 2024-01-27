import requests

api_key = "d04b1d908bc54b6f804cfafd54dd00df"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-12-27&sortBy=publishedAt&apiKey={api_key}"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access to article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
