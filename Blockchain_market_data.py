"""
Pulls Market Data from Blockchain.info
Author: Al Sabay

"""
import requests
import json


r = requests.get("https://api.blockchain.info/charts/market-price?timespan=2year&format=json&sampled=false")

data = json.loads(r.text)

print(len(data["values"]))



