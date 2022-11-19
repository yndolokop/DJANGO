import requests
from datetime import datetime, date
import time
import re
from bs4 import BeautifulSoup
import pprint
import csv

EUROMILLIONS_WEB_BASE_URL = "https://www.euro-millions.com"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=6d22f1d5b66fa1539e3ee2df8b15c77d; InstantCMS[geodata]=a%3A7%3A%7Bs%3A7%3A%22inetnum%22%3Bs%3A27%3A%2246.158.0.0+-+46.159.255.255%22%3Bs%3A7%3A%22country%22%3Bs%3A2%3A%22RU%22%3Bs%3A4%3A%22city%22%3Bs%3A18%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%22%3Bs%3A6%3A%22region%22%3Bs%3A35%3A%22%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D0%BA%D1%80%D0%B0%D0%B9%22%3Bs%3A8%3A%22district%22%3Bs%3A44%3A%22%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9+%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BE%D0%BA%D1%80%D1%83%D0%B3%22%3Bs%3A3%3A%22lat%22%3Bs%3A9%3A%2245.042149%22%3Bs%3A3%3A%22lng%22%3Bs%3A9%3A%2238.980640%22%3B%7D; InstantCMS[logdate]=1577386070; InstantCMS[userid]=00cb7b95006f9aa9c861d9fc32fba967',
    'dnt': '1',
    'Host': 'dedmorozural.ru',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}


def get_draws_by_year(year):
    year_lst = []
    url = EUROMILLIONS_WEB_BASE_URL + '/results-history-' + f"{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    draws = soup.find_all('div', class_='archives')
    for draw in draws:
        date = draw.find('a', class_='title').get('href')  # извлекаем дату
        match = re.sub(r'(\d\d)-(\d\d)-(\d{4})', r'\1/\2/\3', date)  # группирует дату: число, месяц, год. Если нужно.
        match_ = re.search(r'\d\d/\d\d/\d{4}', match)  # ищем дату в объекте с помощью шаблона.
        bal = draw.find('ul', class_='balls small').text  # извлекаем номера лотореи.
        bal = re.findall(r'\d+', bal)  # здесь убираем пробелы сверху и снизу и формируем из soup обычный список.
        ball = [int(i) for i in bal]  # переводим в int.
        ball.insert(0, match_[0])  # добавляем к каждому списку номеров на 1ое место дату.
        year_lst.append(ball)
    # pprint.pprint(year_lst)
    return year_lst


if __name__ == "__main__":
    i = 2004
    final_data = []
    while i <= 2022:
        final_data.extend(get_draws_by_year(i))
        i = i+1
    pprint.pprint(final_data)

    with open('eurom_.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(final_data)

