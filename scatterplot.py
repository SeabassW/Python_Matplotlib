import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [3,5,6,7,8,8,9,3]

plt.scatter(x, y, label='scat', color='r', marker='*')


plt.xlabel('x')
plt.ylabel('y')

plt.show()