import requests.models
from bs4 import BeautifulSoup
import pandas as pd
from .config import SELECTORS


class Parser:
    def __init__(self, response):
        self.response = response

    def parse_products(self):
        response = self.response
        soup = BeautifulSoup(response.content, "html5lib")
        list = []

        print("parsing response...")
        results = soup.find_all('div', attrs= {'class': 'result_right'})
        for result in results:
            item = {}
            item_price = ""
            item_name = result.find('a', attrs= {'class': 'productClickItemV2'})
            span = result.find('span', attrs= {'itemprop': 'price'})

            item_price_text = span.getText()
            if '$' in item_price_text:
                item_price = item_price_text[item_price_text.find('$', 1):]
            else:
                print("unable to find $")


            item['name'] = item_name.getText()
            item['price'] = item_price
            list.append(item)
        return list


    def set_response(self, response):
        self.response = response

    def get_response(self) -> requests.models.Response | None:
        return self.response