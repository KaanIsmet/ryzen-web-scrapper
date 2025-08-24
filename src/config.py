BASE_URL = "https://www.microcenter.com/"
SEARCH_ENDPOINT = "search/"
SEARCH_RESULTS_ENDPOINT = "search_results.aspx?"

#ENSURE ONLY CPU GETS SEARCHED
CATEGORY_CONFIG= "fq=category_flat:Processors%2FCPUs|123&Ntt="
#modify item searched
#use '+' as delimiter
ITEM_SEARCHED = "ryzen+7"

FILE_EXTENSION = "csv"
OUTPUT_FILE = "scraped_data"
DIRECTORY = "data"

#tell parser where to find data on webpage
SELECTORS = {
    'main_article': '#content',
    'article_product_grid': '#productGrid',
    'main': '#mainContent',
    'div_content_results': 'contentResults',
    'ul': 'ul',
    'div_result_right': '.result_right',

}

#https://www.microcenter.com/search/search_results.aspx?
