A = [1, 3, 4, 23, 5]
A1 = [0]*10
A2 = list(range(10))
#print(A)
#print(A1)
#print(A2)

A3 = [i for i in range(10)]
#print(A3)

A4 = [i**2 for i in range(10)]
#print(A4)

from random import randint
A5 = [randint(1, 10) for i in range(10)]
#print(A5)

A6 = [i for i in range(50) if i%2 == 0]
#print(A6)

A7 = [int(input()) for i in range(5)]
#print(A7)

from random import randint
A = [0]*10
for i in range(10):
    A[i] = randint(-50, 50)
    #print(A[i], end=' ')
#print(sep='\d')
x = 50
for i in range(10):
    if A[i] < x:
        x = A[i]
#print(x)
for i in range(10):
    if A[i] > 0:
        #print(A[i])
B = [1, 2, 3]
B.append(4)
print(B)
B.pop(0)
print(B)
B.insert(1, 155)
print(B)