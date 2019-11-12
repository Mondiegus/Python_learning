import numpy as np


np.random.seed(0)
# INPUT = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# numbers = np.random.randint(1,50, size=6, dtype=int)
#
# print(numbers)

# np.random.seed(0)
# arr = np.random.randint(10, size=(16,16))
# arr = np.random.rand(16,16, int)
# arr = arr*10*0.9
# arr = arr.astype(int)
# print(arr)
# output = np.empty([2, 2])
# output = [[INPUT[0][2], INPUT[2][2]], [INPUT[0][0], INPUT[1][0]]]
# print(output)

INPUT = np.array([
    [7, 5, 3, 4, 5],
    [2, 2, 8, 1, 5],
    [3, 8, 8, 4, 4],
    [5, 5, 5, 2, 5],
    [0, 1, 0, 6, 0],
])

input_size = INPUT.shape
output_size = (3, 3)
input_rows = input_size[0]
input_cols = input_size[1]
output_rows = output_size[0]
output_cols = output_size[1]

output = INPUT[int((input_rows-output_rows)/2):int((input_rows+output_rows)/2), int((input_cols-output_cols)/2):int((input_cols+output_cols)/2)]

print(output)

