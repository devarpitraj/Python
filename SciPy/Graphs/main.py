import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order

arr = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 0],
    [0, 1, 0, 1]
])
newarr = csr_matrix(arr)

# connected components
print(connected_components(newarr))

# dijkstra - find the shortest path from one ele to another
print(dijkstra(newarr, return_predecessors=True))
print(dijkstra(newarr, return_predecessors=True, indices=1))

# floyd warshall - shortest path b/w all pairs off elements
print(floyd_warshall(newarr, return_predecessors=True))

# bellman ford - shortest path b/w all pairs of elements and also handles negative values
print(bellman_ford(newarr, return_predecessors=True))

# depth first order - DFS traversal
print(depth_first_order(newarr, 1))

# breadth first order - BFS traversal
print(breadth_first_order(newarr, 1))