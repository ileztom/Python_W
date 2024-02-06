# import numpy as np
#
# a = np.array([[1, 2, 3],[4, 5, 6]])
# print(a)
# print(a.shape)
# print(a[0])
# print(a[0][0])
# print(a[1][2])

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a[1:6:2])
b = np.array([[1, 2, 3, 4][5, 6, 7, 8]])
print(b[0, :2])
print(b[: , 1])
print(b[0, 0])
print(b[1, : : 2])
