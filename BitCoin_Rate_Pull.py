"""
Reads Bitcoin Market Data from Blockchain.info
Author: Vivek Bejugama

"""


#!python
import urllib, json
from datetime import datetime

url = "https://blockchain.info/ticker"
response = urllib.urlopen(url)
data = response.read()

datestring = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

data_str = json.loads(data)

new_rec = {datestring: data_str["USD"]}

with open('C:\\Python27\DataFiles\Bitcoin_USD.txt', "r+") as f:
    data_file = json.load(f)

data_file.update(new_rec)

with open('C:\\Python27\DataFiles\Bitcoin_USD.txt', "w+") as f:
    json.dump(data_file, f)



#json.dump(data, open('C:\\Python27\\DataFiles\\Bitcoin_'+datestring+'.txt', "w"))

#json.dump(data_str["USD"], open('C:\\Python27\DataFiles\Bitcoin_USD.txt', "w"))

# Reading JSON Data
#json_data=open('C:\\Python27\DataFiles\Bitcoin.txt').read()
#Read_data = json.loads(json_data)
#print Read_data



