from .scraper import Scraper
from .config import SELECTORS, BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, CATEGORY_CONFIG

def main():
    print("starting application...")

    resource = Scraper(BASE_URL, SEARCH_ENDPOINT, SEARCH_RESULTS_ENDPOINT, CATEGORY_CONFIG)








if __name__ == "__main__":
    main()