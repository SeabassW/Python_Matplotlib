# Part 1, 2, 3
import matplotlib.pyplot as plt


#Bar charts
# x = [2,4,6,8,10]
# y = [8,2,5,3,7]

# x2 = [1,3,5,7,9]
# y2 = [8,3,1,3,7]

# plt.bar(x, y, label='Bars1', color='c')
# plt.bar(x2, y2, label='Bars2', color='r')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting graph\nCheck it out')
# plt.legend()

# plt.show()

#Histograms
population_ages = [2,23,82,20,84,82,9,15,72,45,32,5,23,120,92,72,56,55,32,11,53,7,23,57,23,67,12,69,1,56,32,25,123,15,23,35,77]

ids = [x for x in range(len(population_ages))]

#plt.bar(ids, population_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')

plt.show()