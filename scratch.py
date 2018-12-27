import requests
import concurrent.futures

base_url = 'https://www.buda.com/api/v2'

url = base_url + '/markets'
response = requests.get(url).json()

market_ids = [coin['id'] for coin in response['markets']]

for market_id in market_ids:
    url = base_url + f'/markets/{market_id}/ticker'
    ticker = requests.get(url).json()['ticker']
    spread = float(ticker['min_ask'][0]) - float(ticker['max_bid'][0])
    print(f"{market_id}: {spread}")