import numpy as np
A = np.array([[3,2,2],
              [3,1,-3],
              [1,0,-2]], dtype=float)
B = np.array([[1,2,0,4],
              [2,0,-1,-2],
              [0,4,1,0]], dtype=float)
tamanoA = np.shape(A)
tamanoB = np.shape(B)
nA = tamanoA[0]
nB = tamanoB[0]
identidadA = np.identity(nA)
identidadB = np.identity(nB)
ABA = np.concatenate((A,identidadA),axis=1)
ABB = np.concatenate((B,identidadB),axis=1)
AB0 = np.copy(ABA)
AB1 = np.copy(ABB)
inversaA = np.copy(ABA[:,nA:])
inversaB = np.copy(ABB[:,nB:])
print('Inversa de A: ')
print(inversaA)
print('Inversa de B: ')
print(inversaB)
