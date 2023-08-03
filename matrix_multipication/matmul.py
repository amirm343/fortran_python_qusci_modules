import matmul
import numpy as np

a = np.array([[1], [0]], order='F')
not_ = np.array([
    [0, 1],
    [1, 0]
], order='F')

print(matmul.matmul(not_, a))