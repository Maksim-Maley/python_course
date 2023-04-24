import requests
from bs4 import BeautifulSoup

print("#1")
response = requests.get('https://automarine.ru/eng/index.html')
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.descendants:
#     if i.name:
#         print(i.name)
print("#2")
print(soup.find(id = "about_us"))

print("#3")
for tag in soup.find_all(['h2','h3','span']):
    print(tag.text)
