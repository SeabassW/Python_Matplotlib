import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [9,8,7,11,4]
eating =   [2,3,1,4,4]
working =  [8,10,12,8,3]
playing =  [5,3,4,1,13]

slices = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c','m','b','g']
plt.pie(slices, 
		labels=activities, 
		colors=colors, 
		startangle=90, 
		shadow=True, 
		explode=(0,0.3,0,0),
		autopct='%1.1f%%')

plt.show()