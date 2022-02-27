import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['name'],
                         data['symbol'],
                         data['url'],
                         data['price']])


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    # trs = soup.find('table', id='currencies').find('tbody').find_all('tr')
    trs = soup.find('table', class_='h7vnx2-2' ).find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        # td3 = tds[2].find('a', class_='cmc-link')
        if len(tds) == 11:
            pass
        else:
            pass




        # symbol = tds[2].find('a').text
        url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
        # price = tds[4].find('a').get('data-usd')
        # price = tds[3].text
        # print(symbol)
        #
        # data = {'name': name,
        #         'symbol': symbol,
        #         'url': url,
        #         'price': price}
        #
        # write_csv(data)



def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
