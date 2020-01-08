import numpy as np
import pandas as pd

X = f"D:\\PngOutput\\training_dataX.npy"
Y = f"D:\\PngOutput\\training_dataY.npy"
training_dataX = np.load(X, allow_pickle=True)

for data in training_dataX:
    print(data)
