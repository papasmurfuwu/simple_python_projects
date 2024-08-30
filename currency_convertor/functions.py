import requests, json 
from config import api_key
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


def search_currency():
    query = input("Please enter the Currency Code, Currency Name or Country: ")
    query_a = query.strip()
    if not query_a or query_a.isdigit():
        return "Please enter a valid string."
    
    query = query.lower()

    for currency in scrape_countries():
        if query == currency['Country'].lower() or \
           query == currency['Currency Name'].lower() or \
           query == currency['Currency Code'].lower(): 
            return f"{currency['Currency Code']} ({currency['Currency Name']}), is the currency code for {currency['Country']}."
    return f"No existing country code for input country..."
        

def get_data(currency):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        print("Error: ", response.status_code)
        return None
    

def exchange(): 
    base_currency = input("Please enter Currency to Exchange (Currency Code): ").lower()
    while True:
        amount = input("Please enter Amount to Exchange (In numbers): ")
        try:
            amount = float(amount)  # Attempt to convert to float
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Error message
    target_currency = input("Please enter Target Currency (Currency Code): ")

    
    exchange_rate = get_data(base_currency)['conversion_rates'][target_currency]
    converted_amount = round(amount * exchange_rate, 2)
    return f"The amount of {amount} {base_currency.upper()} is equivalent to {converted_amount} {target_currency} at an exchange rate of {exchange_rate}."
    

if __name__ == '__main__':
    pass