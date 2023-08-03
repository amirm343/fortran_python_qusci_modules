import tensor_prod as tp
import numpy as np

a = np.array([[1], [0]], order='F')
b = np.array([[1], [0]], order='F')

# myflib.foo(a, b)
print(tp.tp(a, b))