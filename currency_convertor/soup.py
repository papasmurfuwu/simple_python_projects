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
    
    return currencies_ls


def search_currency(query):
    query_a = query.strip()
    print(query)
    if not query_a or query_a.isdigit():
        return "Please enter a valid string."
    
    query = query.lower()

    for currency in scrape_countries():
        if query == currency['Country'].lower() or \
           query == currency['Currency Name'].lower() or \
           query == currency['Currency Code'].lower(): 
            return f"{currency['Currency Code']} ({currency['Currency Name']}), is the currency code for {currency['Country']}."
    return f"No existing country code for input country..."
        
user_input = input("Please enter the Currency Code, Currency Name or Country: ")
print(search_currency(user_input))


