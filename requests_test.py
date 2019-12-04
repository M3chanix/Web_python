import requests
result = requests.get("https://ru.wikipedia.org/wiki/Университет_ИТМО")
print(result.content)
print(result.text)
print(result.json)
