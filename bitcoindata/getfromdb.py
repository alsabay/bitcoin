from pymongo import MongoClient
import urllib2

client = MongoClient()
db = client['okcoindb']
collection = db['prices']

pricelist = list()
for doc in collection.find():
    try:
        p = doc['price']
        pricelist.append(p)
    except:
        print 'done'
        exit()
    f = open("/Users/Olivia/SMUDS/MSDS7330/termproject/bitcoindata/theprices.txt", "w")
    f.write(str(pricelist))
    f.close()
