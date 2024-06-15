import requests

api_key = "2f35f7f88e3d49f9b38448972520fb0f"

url = ("https://newsapi.org/v2/everything?q=tesla&from=" \
       "2024-05-15&sortBy=publishedAt&apiKey=" \
       "2f35f7f88e3d49f9b38448972520fb0f")

#make request
request = requests.get(url)

#get a dictionary with data
content = request.json()

#access the article titles and description
for article in content["articles"]:
       print(article["title"])
       print(article["description"])

print("hello")