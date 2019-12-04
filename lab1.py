import requests
import re
import os
#os.chdir(~/study/web-python/)

http_page = requests.get("https://ru.wikipedia.org/wiki/Университет_ИТМО").text
pattern = re.compile("<h3>.*Поддержка стартапов.+</h3>[\S\s]*(<dl><dt>Гранты[\S\s]*?)<h3>")
result = pattern.findall(http_page)
href_pattern = re.compile("<[\s\S]+?>")
href = href_pattern.findall(result[0])
result = href_pattern.sub("", result[0])
result = re.sub("(&#[0-9]+;[0-9]+|&#[0-9]+;)", "", result)

with open("lab1_result.txt", 'w') as f:
    f.write(result)

