# Triangulation
# Delaunay() method

from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()

# Convex Hull - smallest polygon that covers all of the given points
from scipy.spatial import ConvexHull

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0], points[:, 1])

for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    
plt.show()

# KDTrees - datastructure optimized for nearest neighbor queries

from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

# Distance Matrix

# Euclidean Distance
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)
print(f"Euclidean Distance between {p1} and {p2} is {res}")

# Cityblock Distance(Manhattan Distance)
from scipy.spatial.distance import cityblock

res = cityblock(p1, p2)
print(f"Cityblock Distance between {p1} and {p2} is {res}")

# Cosine Distance
from scipy.spatial.distance import cosine

res = cosine(p1, p2)
print(f"Cosine Distance between {p1} and {p2} is {res}")

# Hamming Distance
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)
print(res)