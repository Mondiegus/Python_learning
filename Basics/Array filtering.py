import numpy as np

np.random.seed(0)
arr = np.random.randint(0,1025, size=(50,50), dtype=int)
numbers = list(2**x for x in range(1, 11))

B = arr[np.isin(arr, numbers)]
B = np.sort(B)[::-1]

print(B)

