import myflib
import numpy as np

a = np.array([[1], [0]], order='F')
b = np.array([[0], [1]], order='F')

# myflib.foo(a, b)
print(myflib.foo(a, b))