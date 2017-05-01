# part 9, 10, 12, 13
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np
import urllib

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
	stock_price_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
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
	#3: Fill in / customize axis
	ax1.plot_date(date, close_p, '-', label='Price')
	ax1.axhline(close_p[0], color='k', linewidth=3)			#Horizontal line. Vertical also possible

	## Fill in area for profit / loss
	ax1.fill_between(date, close_p, close_p[0], where=(close_p > close_p[0]), facecolor='g', alpha=0.5)
	ax1.fill_between(date, close_p, close_p[0], where=(close_p < close_p[0]), facecolor='r', alpha=0.5)

	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.grid(True, color='grey', linestyle='-', linewidth=0.5)
	ax1.xaxis.label.set_color('c')
	ax1.yaxis.label.set_color('r')
	ax1.set_yticks([0,10,20,30,40])
	ax1.tick_params(axis='x', colors='#f06215')

	ax1.spines['left'].set_color('g')
	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)




	#4: Apply plt 
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.93, wspace=0.2, hspace=0)
	plt.show()

graph_data('EBAY')