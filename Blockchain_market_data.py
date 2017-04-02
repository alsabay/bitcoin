"""
Pulls Market Data from Blockchain.info
Author: Al Sabay

"""
import requests
import json
import time

# volume
#dv = requests.get("https://api.blockchain.info/charts/trade-volume?timespan=2year&format=json&sampled=false")

# prices
dp = requests.get("https://api.blockchain.info/charts/market-price?timespan=2year&format=json&sampled=false")

f = open('data/marketPrice.json', "w")
f.write(dp.text)
f.close()

#f = open('data/marketPrice.json',"r")
#df = json.load(f)
#f.close()

