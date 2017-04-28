import matplotlib.pyplot as plt
import numpy as np

#Part 1: Using csv library
"""
import csv 

x = []
y = []

with open('example.txt', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x,y, label='loaded from csv')
"""
#Part 2: Using numpy
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='loaded from csv')

plt.xlabel('x')
plt.ylabel('y')

plt.show()