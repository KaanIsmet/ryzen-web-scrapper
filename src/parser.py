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
        result_right = soup.find_all('div', attrs= {'class': 'result_right'})
        print(result_right)

    def set_response(self, response):
        self.response = response

    def get_response(self) -> requests.models.Response | None:
        return self.response