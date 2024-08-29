import requests
from bs4 import BeautifulSoup



def scrape_countries():
    url = 'https://www.exchangerate-api.com/docs/supported-currencies'
    page = requests.get(url)    
    soup = BeautifulSoup(page.content, 'html.parser')
    currency_info = {}
    currencies_ls = []

    text = soup.find("u", string="All Supported Currencies")
    table = text.find_parent().find_next_sibling().find_next_sibling()
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        currency_info = {
            "Currency Code": cells[0].get_text(),
            "Currency Name": cells[1].get_text(),
            "Country": cells[2].get_text()
        }
        currencies_ls.append(currency_info)
    
    
# If user donese't know currency code, allow them to use Country to search for code

scrape_countries()