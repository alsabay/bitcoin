"""
Pulls Market Data from Blockchain.info
Author: Al Sabay

"""
import requests
import json


dv = requests.get("https://api.blockchain.info/charts/trade-volume?timespan=2year&format=json&sampled=false")

#dp = requests.get("https://api.blockchain.info/charts/market-price?timespan=2year&format=json&sampled=false")

data = json.loads(dv.text)
print(data)

#print(len(data["values"]))



