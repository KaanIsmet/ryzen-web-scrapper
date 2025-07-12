from .scraper import Scraper
from .config import SELECTORS, BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, CATEGORY_CONFIG, ITEM_SEARCHED, OUTPUT_FILE, DIRECTORY
from .parser import Parser
from .storage import Storage

def main():
    print("starting application...")

    response = Scraper(BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, ITEM_SEARCHED ,CATEGORY_CONFIG)
    parser = Parser(response)

    list = parser.parse_products()

    storage = Storage(DIRECTORY)
    storage.save_to_csv(list, OUTPUT_FILE)
    print(storage.load_from_csv(OUTPUT_FILE))








if __name__ == "__main__":
    main()