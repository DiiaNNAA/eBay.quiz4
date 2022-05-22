import re
import csv
import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup

h = {"Accept-Language": "en-US", "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0"}
file = open('eBay.csv', 'w', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(["Product_name", "Price_from", "Price_to"])

for ind in range(1, 25):
    url = 'https://www.ebay.co.uk/e/_electronics/best-selling-new-phones?_pgn='+str(ind)
    r = requests.get(url, headers=h)
    # print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup_section = soup.find('ul', class_='b-list__items_nofooter')
    all_products = soup_section.find_all('li', class_='s-item s-item--large')

    for product in all_products:
        product_name = product.h3.text
        product_name_without_specialchar = re.sub('[^a-zA-Z0-9\n\.]', ' ', product_name)
        # print(product_name_without_specialchar)
        price_range = product.find('span', class_='s-item__price').text
        price_from = price_range.split(' ')[0]
        try:
            price_to = price_range.split(' ')[2]
        except IndexError:
            price_to = None
        file_obj.writerow([product_name_without_specialchar, price_from, price_to])
    sleep(randint(1, 15))


