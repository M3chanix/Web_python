from bs4 import BeautifulSoup
import requests
import re
import sqlite3

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

conn = sqlite3.connect("web.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO Itmo VALUES (?, ?)", data)
conn.commit()
cursor.close()
conn.close()
