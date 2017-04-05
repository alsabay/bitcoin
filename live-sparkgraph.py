"""
live graph animation from a bitcoin ticker file Apache Spark Version
Author: Al Sabay

"""
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
from pyspark.sql import SparkSession

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

#Create SparkSession object
my_spark = SparkSession.builder.appName('myApp').config("spark.mongodb.input.uri", "mongodb://127.0.0.1/okcoindb.prices") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/okcoindb.prices").getOrCreate()
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://127.0.0.1/okcoindb.prices").load()

def animate(i):
    xs = []
    ys = []
    ptl = []
    dtl = []
    dtl = df.select('date').rdd.flatMap(lambda x: x).collect()
    # convert unix dates
    for item in dtl:
        xs.append(dt.datetime.fromtimestamp(item))
    # get prices from rdd
    ys = df.select('price').rdd.flatMap(lambda x: x).collect()

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
        ani = animation.FuncAnimation(fig, animate, interval=500)
        plt.show()
    except KeyboardInterrupt:
        print('Terminated Plotting')
if __name__ == '__main__':
    main()

