## Part 14, 17, 18
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib
import datetime as dt

style.use('ggplot')


def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter

def graph_data(stock):

	#1: Define figure and axis
	fig = plt.figure() 			# for customization, a reference to figure is needed
	ax1 = plt.subplot2grid((1,1), (0,0))

	#2: Define data
	stock_price_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
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

	x = 0
	y = len(date)
	ohlc = []

	while x < y:
		append_me = date[x], open_p[x], high_p[x], low_p[x], close_p[x], volume[x]
		ohlc.append(append_me)
		x+=1

	candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')


	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
	ax1.grid(True)

	## Apply text to graphs
	font_dict = {'family': 'serif',
				'color': 'darkred',
				'size': 15}
	ax1.text(date[5], close_p[1], 'Ebay Prices', font_dict)

	## Apply annotation to graph
	ax1.annotate('Bad news!', (date[11], high_p[11]), 
				xytext=(0.8, 0.9), textcoords='axes fraction',
				arrowprops = dict(facecolor='k', color='grey'))

	#4: Apply plt 
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.93, wspace=0.2, hspace=0)
	plt.show()

graph_data('EBAY')