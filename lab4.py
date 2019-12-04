from bs4 import BeautifulSoup
import requests
import re
import psycopg2

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

conn = psycopg2.connect(dbname='Itmo', user='db_user', password='user_password', host='localhost')
with conn.cursor() as cursor:
    conn.autocommit = True
    insert = sql.SQL('INSERT INTO Itmo VALUES {}').format(
        sql.SQL(',').join(map(sql.Literal, data))
    )
    cursor.execute(insert)
conn.close()
