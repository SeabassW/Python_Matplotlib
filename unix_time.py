# Part 11
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import numpy as np
import urllib
import datetime as dt

def graph_data(stock):

	#1: Define figure and axis
	fig = plt.figure() 			# for customization, a reference to figure is needed
	ax1 = plt.subplot2grid((1,1), (0,0))

	#2: Define data
	stock_price_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
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
															unpack=True)
	# Convert unix time to datetime
	dateconv = np.vectorize(dt.datetime.fromtimestamp)
	date = dateconv(date)


	#3: Fill in / customize axis
	ax1.plot_date(date, close_p, '-', label='Price')
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.grid(True, color='g', linestyle='-')

	#4: Apply plt 
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.93, wspace=0.2, hspace=0)
	plt.show()

graph_data('TSLA')