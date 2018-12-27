import requests
import concurrent.futures as futures

base_url = 'https://www.buda.com/api/v2'

url = base_url + '/markets'
response = requests.get(url).json()

market_ids = [coin['id'] for coin in response['markets']]

# for market_id in market_ids:
#     url = base_url + f'/markets/{market_id}/ticker'
#     ticker = requests.get(url).json()['ticker']
#     spread = float(ticker['min_ask'][0]) - float(ticker['max_bid'][0])
#     print(f"{market_id}: {spread}")

def get_ticker(market_id, base_url):
    url = base_url + f'/markets/{market_id}/ticker'
    return requests.get(url).json()['ticker']

with futures.ThreadPoolExecutor(max_workers=8) as executor:
    # Start the load operations and mark each future with its market id
    future_to_id = {executor.submit(get_ticker, market_id, base_url): market_id for market_id in market_ids}
    for future in futures.as_completed(future_to_id):
        market_id = future_to_id[future]
        try:
            ticker = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (id, exc))
        else:
            spread = float(ticker['min_ask'][0]) - float(ticker['max_bid'][0])
            print(f"{market_id}: {spread}")