import matplotlib.pyplot as pyplot 
import matplotlib.dates as mdates
import numpy as numpy
import urllib


def graph_data(stock):

	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'﻿

	source_code = urllib.request.urlopen(stock_price_url).read().decode()

	stock_data = []
	split_source = source_code.split('\n')

	for line in split_source:
		split_line = line.split(',')
		if len(split_line) == 6:
			if 'values' not in line:
				stock_data.append(line)

	date, close_p, high_p, low_p, open_p, volume = np.loadtxt(stock_data, 
															delimiter=',', 
															unpack=True, 
															# %Y = full year. 2015
															# %y = partial year 15
															# $m = number month
															# %d = number day
															# %H = hours
															# %M = minutes
															# %S = seconds
															# 12-06-2014 = %m-%d-%Y
															converters={0: bytespdate2num('%Y%m%d')})

	plt.plot(x,y, label='loaded from csv')

	plt.xlabel('x')
	plt.ylabel('y')

	plt.show()

graph_data('TSLA')