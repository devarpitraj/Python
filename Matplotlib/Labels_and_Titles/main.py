import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 9, 3, 8, 2, 6])
y = np.array([4, 9, 2, 7, 1, 0])

plt.plot(x, y)

# xlabel() and ylabel()
plt.xlabel("Avg")
plt.ylabel("Amount")

# plt.show()

# title()
plt.title("Sports")
# plt.show()

# font property
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("FGH", fontdict = font1)
plt.xlabel("AC", fontdict = font2)
plt.ylabel("BH", fontdict = font2)
# plt.show()

# title location
plt.title("HJKJK", loc = 'right')
plt.show()