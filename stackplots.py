import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [9,8,7,11,4]
eating =   [2,3,1,4,4]
working =  [8,10,12,8,3]
playing =  [5,3,4,1,13]

# stackplot can't have labels, therefor this workaround
plt.plot([],[], color ='m', label='Sleeping', linewidth=5)
plt.plot([],[], color ='c', label='Eating', linewidth=5)
plt.plot([],[], color ='r', label='Working', linewidth=5)
plt.plot([],[], color ='k', label='Playing', linewidth=5)


plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
plt.legend()
plt.show()