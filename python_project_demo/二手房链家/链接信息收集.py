# author:yangleiw
# createdate:2022/5/21

import requests
from bs4 import BeautifulSoup

page = 10
for i in range(1, 10):
    url = "https://nc.lianjia.com/ershoufang/pg" + str(i)
    print(url)
    resp = requests.get(url)
    # resp.encoding = resp.apparent_encoding  # 自动识别编码，防止乱码
    resp.encoding = 'utf-8'
    html = resp.text
    # print(resp)
    soup = BeautifulSoup(html, 'html.parser')  # lxml更快
    infos = soup.find('ul', {'class': 'sellListContent'}).find_all('li')
    with open(r"lianjia.csv", "a", encoding='utf-8') as f:
        for info in infos:
            name = info.find('div', {'class': 'title'}).find('a').get_text()
            price = info.find('div', {'class': 'priceInfo'}).find('span').get_text()
            address = info.find('div', {'class': 'address'}).find('div').get_text()

            # print(name, price, address)

            f.write('{},{},{}\n'.format(name, price, address))
