import numpy as np
A = np.array([True, False, True, False])
B = np.array([True, True, False, False])

print(np.logical_and(A, B)) #И
print(np.logical_or(A, B)) #ИЛИ
print(np.logical_not(A, B)) #НЕ
print(np.logical_xor(A, B)) #ИСКЛЮЧАЮЩЕЕ ИЛИ

C = np.array([1, 0, 2, 0])
D = np.array([3, 4, 0, 0])
print()
print(np.logical_and(C, D))