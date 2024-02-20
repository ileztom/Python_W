import numpy as np

A = np.array([1,2,3,4,5,6,7])
a = A > 5
print(A[a])
print((A[A > 5]))
print()
B = np.array([1,2,3,4,5,6,7])
print(A == B)
print(A != B)
print(A > B)
print(A < B)
print(np.greater(A, B)) # A > B
if np.array_equal(A, B): #если оба массива равны по длине и все элементы равны
    print("A == B")
if np.any(A > B): #хотя бы один элемент удовлетворяет условию
    print("+")
if np.all(A > 0): #если все элементы удовлетворяют условию
    print("True")
C = np.array([1,2,np.inf])
print(C * 0)
D = C * 0
print(D.sum())