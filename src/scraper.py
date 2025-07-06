import requests

def Scraper(base_url: str, search_endpoint: str, search_results_endpoint: str, category_config: str):

    url = base_url + search_endpoint + search_results_endpoint + category_config

    response = requests.get(url)

    if response.ok:
        return response
    else:
        print("Unable to request url")
        return ""