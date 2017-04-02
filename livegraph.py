"""
live graph animation from a bitcoin ticker file
Author: Al Sabay

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
import datetime as dt
import matplotlib.dates as mdates
import json

style.use('fivethirtyeight')

fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
ax1 = plt.subplot2grid((1,1), (0,0))

#open json file with market data
f = open('data/marketPrice.json', 'r')
df = json.load(f)
f.close()

def animate(i):
    xs = []
    ys = []
    for i in df['values']:
        ys.append(i['y'])
        #convert unix time to date
        date = dt.datetime.fromtimestamp(i['x'])  
        xs.append(date)
    ax1.clear()
    ax1.plot_date(xs, ys,fmt = '-', label = 'Price')
    # start, end = ax1.get_xlim()
    # major_ticks = np.arange(start,end,50)
    # minor_ticks = np.arange(start,end,5)
    # ax1.set_xticks(major_ticks)
    # ax1.set_xticks(minor_ticks, minor=True)
    # ax1.set_yticks(major_ticks)
    # ax1.set_yticks(minor_ticks, minor=True)
    # ax1.grid(which='both')
    # ax1.grid(which='minor', alpha=0.2)
    # ax1.grid(which='major', alpha=0.5)
    for label in ax1.get_xticklabels():
        label.set_rotation(45)
    ax1.grid(color='c', linestyle='-', linewidth=1)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Bitcoin Price')
#plt.xlabel('Date', fontsize=15)
#plt.ylabel('Bitcoin Price', fontsize=15)
fig.suptitle('Bitcoin Price Graph', fontsize=20)
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
