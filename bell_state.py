from time import time

import operators.matrix_multipication.matmul as matmul
import operators.tensor_product.tensor_prod as tp

import numpy as np

bt = time()

ket0 = np.array([[0], [1]], order='F')
ket1 = np.array([[1], [0]], order='F')

a = ket0
b = ket1

psi = tp.tp(a,b)

# print(psi)

i = np.array([
    [1, 0],
    [0, 1]
], order='F')

hadamard = (1/np.sqrt(2))*np.array([
    [1, 1],
    [1, -1]
], order='F')

hi = tp.tp(hadamard, i)

psi = matmul.matmul(hi, psi)

c_not = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], order='F')

psi = matmul.matmul(c_not, psi)

print(psi)

et = time()
print(et-bt)