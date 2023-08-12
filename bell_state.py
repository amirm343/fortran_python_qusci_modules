from time import time

import matmul
import numpy as np

bt = time()

ket0 = np.array([[1], [0]], order='F')
ket1 = np.array([[0], [1]], order='F')

a = ket0
b = ket1

psi = fop.tensor_product.tp(a,b)

i = np.array([
    [1, 0],
    [0, 1]
], order='F')

hadamard = (1/np.sqrt(2))*np.array([
    [1, 1],
    [1, -1]
], order='F')

hi = fop.tensor_product.tp(hadamard, i)

psi = fop.matrix_multipication.matmul(hi, psi)

c_not = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], order='F')

psi = fop.matrix_multipication.matmul(c_not, psi)

print(psi)

et = time()
print(et-bt)