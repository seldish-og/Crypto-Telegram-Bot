import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.URL = 'https://ru.tradingview.com/ideas/'
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                 ' Chrome/87.0.4280.141 Safari/537.36',
                   'accept': '*/*'}
        self.HOST = 'https://ru.tradingview.com'

    def get_html(self, page):  # get html page code
        url = self.URL + f'page-{page}'
        req = requests.get(url, headers=self.HEADERS)
        return req

    def get_link(self, user_crypto):
        page = 1
        while True:
            html = self.get_html(page).text
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all('div', class_='tv-feed-layout__card-item')
            for item in items:
                title = item.find('a', class_='tv-widget-idea__symbol').get_text(strip=True)
                link = self.HOST + item.find('a', class_='tv-widget-idea__title').get('href')
                if user_crypto in title:
                    return link
            page += 1

