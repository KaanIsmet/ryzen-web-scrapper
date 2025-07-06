BASE_URL = "https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt="
SEARCH_ENDPOINT = "search/"
SEARCH_RESULTS_ENDPOINT = "search_results.aspx?Ntt="

#ENSURE ONLY CPU GETS SEARCHED
CATEGORY_CONFIG= "Ntx=mode+MatchPartial&Ntk=all&sortby=match&N=4294804349&myStore=true"
#modify item searched
#use '+' as delimiter
ITEM_SEARCHED = "ryzen+7+cpu"

FILE_EXTENSION = "csv"
OUTPUT_FILE = "scraped_data.csv"

#tell parser where to find data on webpage
SELECTORS = {
    'main_article': '#content',
    'article_product_grid': '#productGrid',
    'main': '#mainContent',
    'div_content_results': 'contentResults',
    'ul': 'ul',
    'div_result_right': '.result_right',

}