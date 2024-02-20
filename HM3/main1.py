import numpy as np
A = np.array([1,2, np,nan, np.inf, -np.inf])
print(np.isinf(A))
print(np.isinf(A))

B = np.isinf(A)
print(A[~B])
C = np.isnan(A)
print(A[~C])