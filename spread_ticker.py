import requests
import concurrent.futures as futures

class SpreadTicker:
    BASE_URL = 'https://www.buda.com/api/v2/markets'

    def __init__(self):
        response = requests.get(self.BASE_URL).json()
        self.market_ids = [coin['id'] for coin in response['markets']]
        self.spreads = {}

    def get_ticker(self, market_id):
        url = self.BASE_URL + f'/{market_id}/ticker'
        return requests.get(url).json()['ticker']

    def spread_stream(self):
        with futures.ThreadPoolExecutor(max_workers=20) as executor:
            # Start the load operations and mark each future with its market id
            future_to_id = {executor.submit(self.get_ticker, market_id): market_id for market_id in self.market_ids}
            for future in futures.as_completed(future_to_id):
                market_id = future_to_id[future]
                try:
                    ticker = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (id, exc))
                else:
                    spread = float(ticker['min_ask'][0]) - float(ticker['max_bid'][0])
                    self.spreads[market_id] = spread

if __name__ == "__main__":
    t = SpreadTicker()
    t.spread_stream()
    print(t.spreads)
