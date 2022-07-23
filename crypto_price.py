from bs4 import BeautifulSoup
import requests
from forex_python.converter import CurrencyRates

# Need to change this as it is very slow
c = CurrencyRates()
usd_to_eur = (c.get_rate('USD', 'EUR'))

def _get_url(name_of_coin):
  """ Private function to retrieve the URL page of a coin """ 
    
    return 'https://coinmarketcap.com/currencies/' + name_of_coin
    

def get_price(name_of_coin):
  """ 
  Need to convert this to *args to allow for multiple coins.
  
  """
    
    coin_url = _get_url(name_of_coin)
    cmc = requests.get(coin_url)
    soup = BeautifulSoup(cmc.content, 'html.parser')
    abc = soup.find("div", {"class": "priceValue"}).get_text(strip=True)
    if "," in abc:
        abc = abc.replace(',','') 
    abc = float(abc.replace('$',''))    
    return usd_to_eur*abc
     
    
get_price('bitcoin')    
