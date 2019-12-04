from bs4 import BeautifulSoup
import requests
import re
import pymysql
from contextlib import closing

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

with closing(pymysql.connect(host='localhost', user='user', password='password', db='Itmo')) as conn:
    with conn.cursor() as cursor:
        query = 'INSERT INTO Itmo VALUES (%s, %s)'
        cursor.executemany(query, data)
        conn.commit()
