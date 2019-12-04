from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient

http_page = requests.get("https://ru.wikipedia.org/wiki/Университет_ИТМО").text
soup = BeautifulSoup(http_page, "html.parser")
tag = soup.find('dl', text="Гранты, бизнес-инкубаторы, коворкинги")
siblings = tag.find_next_siblings()
true_siblings = []
for sibling in siblings:
    if sibling.name =='h3':
        break
    true_siblings.append(sibling.text)

data = []

for text in true_siblings:
    year = re.findall("^.+?([0-9]{4})", text)
    data.append((str(year[0]), str(text)))

post_list = []
post_attributes = ['year', 'text']

for i in data:
    d = {a: b for a,b in zip(post_attributes, i)}
    post_list.append(d)

client = MongoClient()
db = client['Itmo']
posts = db['posts']
posts.insert_many(post_list)

