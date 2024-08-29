import requests, json 
from config import api_key

def get_data(currency):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)

    else:
        print("Error: ", response.status_code)
        return None
    
def search_currency(query):
    query = query.strip().lower()
    

# Have soup scrape in parallel such will not hinder main service
# User interface (tkinter or sth) 