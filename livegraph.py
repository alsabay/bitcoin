"""
live graph animation from a bitcoin ticker file
Author: Al Sabay

"""
import iomongo
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
import datetime as dt
import matplotlib.dates as mdates
import json
import requests
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler

style.use('fivethirtyeight')
mDB = iomongo.IO_mongo()
fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
ax1 = plt.subplot2grid((1,1), (0,0))

#open json file with market data
#f = open('data/marketPrice.json', 'r')
#df = json.load(f)
#f.close()

def animate(i):
    mjstring = mDB.load('price')
    xs = []
    ys = []
    #for i in df['values']:
    #    ys.append(i['y'])
    #    #convert unix time to date
    #    date = dt.datetime.fromtimestamp(i['x'])
    #    xs.append(date)

    for doc in mjstring :
        ys.append(doc['price'])
        #convert unix time to date
        date = dt.datetime.fromtimestamp(doc['date'])
        xs.append(date)
    ax1.clear()
    ax1.plot_date(xs, ys,fmt = '-', label = 'Price')
    # turn x axis date labels 45 degrees
    for label in ax1.get_xticklabels():
        label.set_rotation(45)
    ax1.grid(color='c', linestyle='-', linewidth=1)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Bitcoin Price')
fig.suptitle('Bitcoin Price Graph', fontsize=20)
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

def main():
    try:
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
    except KeyboardInterrupt:
        print('Terminated Plotting')
if __name__ == '__main__':
    main()
        
