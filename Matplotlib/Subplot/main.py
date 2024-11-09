import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2, 0, 6, 1])
y1 = np.array([4, 2, 0, 6])
x2 = np.array([6, 2, 8, 3, 1])
y2 = np.array([6, 0, 8, 2, 4])

# 2 plot sideways
# plot 1
# plt.subplot(1, 2, 1)
# plt.plot(x1, y1)
# plt.title("Salary")

# # plot 2
# plt.subplot(1, 2, 2)
# plt.plot(x2, y2)
# plt.title("Dues")

# plt.suptitle("Employee")
# # plt.show()

# 2 plot up down
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)

# plt.subplot(2, 1, 2)
# plt.plot(x2, y2)

# plt.show()

# multiple plots
y1 = np.array([3, 8, 5])
plt.subplot(2, 3, 1)
plt.plot(y1)

y2 = np.array([3, 8])
plt.subplot(2, 3, 2)
plt.plot(y2)

y3 = np.array([3, 8, 5, 7])
plt.subplot(2, 3, 3)
plt.plot(y3)

y4 = np.array([0, 1, 5, 3, 4])
plt.subplot(2, 3, 4)
plt.plot(y4)

y5 = np.array([1, 9, 2, 4])
plt.subplot(2, 3, 5)
plt.plot(y5)

y6 = np.array([6, 2, 0])
plt.subplot(2, 3, 6)
plt.plot(y6)

plt.show()