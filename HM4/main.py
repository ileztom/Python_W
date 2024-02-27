import numpy as np

# A = np.empty(10) #производные элементы
# print(A)
# B = np.empty(10, dtype="int16")
# print(B)
# C = np.empty(10, dtype="float32")
# print(C)
# D = np.eye(4) #диагональ 1, остальные элементы 0
# print(D)
# E = np.identity(5) #Квадратный массив, диагональ 1, остальные 0
# print(E)

# A = np.mat("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
# print(A)
# B = np.mat("1, 2, 3, 4; 5, 6, 7, 8")
# print(B)
# C = np.diag([1, 2, 3])
# print(C)
# D = np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print(D)
# E = np.tri(4)
# print(E)
# F = np.vander([1, 2, 3])
# print(F)

# A = np.linspace(0, np.pi, 0)
# print(A)
# B = np.logspace(0, 1, 3)
# print(B)
# C = np.geomspace(1,4,3)
# print(C)

A = np.array([[11, 32, 23, 15], [41, 15, 36, 29], [34, 18, 11, 25]])
A1 = np.where(A%2==0, A, 5)
print(A1)