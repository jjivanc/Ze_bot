import requests
from bs4 import BeautifulSoup
import bot

req = requests.get('https://nhentai.net/g/{text}/)
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
title = soup.find(name='title')
imagens = soup.find_all(name='img', attrs={'class':'lazyload'})

print(title)

for image in imagens:
    print(image['data-src'])
