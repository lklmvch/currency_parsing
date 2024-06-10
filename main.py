import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


def get_info():
    url = f'https://myfin.by/currency/minsk'
    response = requests.get(url, headers=headers)
    sleep(4)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('span', class_='accent')[:6]

    usd_give = data[0].text.strip()
    usd_get = data[1].text.strip()
    euro_give = data[2].text.strip()
    euro_get = data[3].text.strip()
    rub_give = data[4].text.strip()
    rub_get = data[5].text.strip()
    yield '', usd_give, usd_get, euro_give, euro_get, rub_give, rub_get










