import numpy as np
from scipy.sparse import csr_matrix

# create csr matrix from an array
arr = np.array([0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr))

# viewing stored data
print(csr_matrix(arr).data)

# counting non-zero
print(csr_matrix(arr).count_nonzero())

# removing zero-entries
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

# eliminate duplicate entries
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

# converting csr to csc
newarr = csr_matrix(arr).tocsc()
print(newarr)