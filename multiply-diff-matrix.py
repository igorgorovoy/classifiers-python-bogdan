import numpy as np

# Define two arrays with different dimensions
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

result = a * b
#result = a * b[:, np.newaxis]

print(result)