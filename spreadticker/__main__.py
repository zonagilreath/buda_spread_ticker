import argparse
from spreadticker import SpreadTicker

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--concurrency", type=int, required=False,
                        help='determine maximum threads; default is cpu-count * 5')
    args = parser.parse_args()

    t = SpreadTicker(max_threads=args.concurrency)
    t.spread_stream()
    print(t.spreads)

if __name__ == '__main__':
    main()