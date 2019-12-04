from bs4 import BeautifulSoup
import requests
import re

http_page = requests.get("https://ru.wikipedia.org/wiki/Университет_ИТМО").text
soup = BeautifulSoup(http_page, "html.parser")
tag = soup.find('dl', text="Гранты, бизнес-инкубаторы, коворкинги")
siblings = tag.find_next_siblings()
with open("lab2_result.txt", 'w') as f:
    for sibling in siblings:
        if sibling.name == 'h3':
            break
        f.write(sibling.text)

#with open("lab1_result.txt", 'w') as f:
#    f.write(result)

