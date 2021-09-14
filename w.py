import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get("https://habr.com/ru/all/")
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    date = article.find('span', class_='tm-article-snippet__datetime-published').text
    title = article.h2.text.lower()
    body = article.find(class_='article-formatted-body').text.lower()
    hub = article.find_all('span', class_='tm-article-snippet__hubs-item')
    hub_text = [hub.text for hub in hub]
    link = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
    url = "https://habr.com" + link
    res = requests.get(url)
    full_body = BeautifulSoup(res.text, 'html.parser')
    result = full_body.find_all(class_='article-formatted-body_version-2')
    full_body_text = [result.text.lower() for result in result]

    for word in KEYWORDS:
        if (word in title or word in hub_text or word in body or word in full_body_text):
            print(f'Дата: {date} - Заголовок: {title} - Ссылка: {url}')





