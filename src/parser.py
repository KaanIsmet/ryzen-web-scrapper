from bs4 import BeautifulSoup
import pandas as pd
from .config import SELECTORS
class Parser:
    def parse_products(self, response):

        soup = BeautifulSoup(response.content, "html5lib")
        list = []
    # for product in soup.select(SELECTORS['div_result_right']):

        # data = {
        #     'name':
        #     'price':
        # }

