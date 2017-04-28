# Part 1, 2
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]


plt.plot(x,y, label='First')
plt.plot(x2,y2, label='Second')
plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting graph\nCheck it out')
plt.legend()


plt.show()
