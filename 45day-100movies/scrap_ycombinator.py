from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)
website = response.text

soup = BeautifulSoup(website, "html.parser")

article_texts = []
article_links = []
article_tag = soup.select(selector=".titleline > a")

for t in article_tag:
    text = t.getText()
    article_texts.append(text)
    link = t.get("href")
    article_links.append(link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

high_number = max(article_upvotes)
high_index = article_upvotes.index(high_number)
print(article_texts[high_index], article_links[high_index])
