import requests
from bs4 import BeautifulSoup

URL = 'https://ru.tradingview.com/ideas/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/87.0.4280.141 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://ru.tradingview.com'


def get_html(url, params=None): # get html page code
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html): # return list with dictionaries [{cryptoTitle: articleTitle, link: articleLink}, ...]
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='tv-feed-layout__card-item')
    currency = []
    for item in items:
        currency.append({
            'title': item.find('div', class_='tv-widget-idea__info-row').get_text(strip=True),
            'link': HOST + item.find('a', class_='tv-widget-idea__title').get('href')
        })
    return currency


def result():
    return get_content(get_html(URL).text)
