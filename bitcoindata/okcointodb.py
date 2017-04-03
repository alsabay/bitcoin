##TAKEN FROM: https://github.com/stavros0/bitcoin-price-prediction/blob/master/bitcoin_price_prediction/okcoin.py

"""Script to gather market data from OKCoin Spot Price API."""
import requests
from pytz import utc
from datetime import datetime
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler

client = MongoClient()
database = client['okcoindb']
collection = database['prices']


def tick():
    """Gather market data from OKCoin Spot Price API and insert them into a
       MongoDB collection."""
    ticker = requests.get('https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd').json()
    depth = requests.get('https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=60').json()
    date = datetime.fromtimestamp(int(ticker['date']))
    price = float(ticker['ticker']['last'])
    collection.insert({'date': date, 'price': price})
    print(date, price)


def main():
    """Run tick() at the interval of every ten seconds."""
    scheduler = BlockingScheduler(timezone=utc)
    scheduler.add_job(tick, 'interval', seconds=10)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
