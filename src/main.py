from .scraper import Scraper
from .config import SELECTORS, BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, CATEGORY_CONFIG, ITEM_SEARCHED
from .parser import Parser

def main():
    print("starting application...")

    response = Scraper(BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, ITEM_SEARCHED ,CATEGORY_CONFIG)
    parser = Parser(response)

    parser.parse_products()







if __name__ == "__main__":
    main()