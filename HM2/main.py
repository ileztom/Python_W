import numpy as np
#ex1
array = np.arange(27).reshape(3, 3, 3)
print(np.sum(array, axis=2))
#ex2
array = np.arange(20).reshape(4, 5)
second_array = np.arange(5)
print(array * second_array)
#ex3
array = np.random.randint(2, 6, (10))
print(np.unique(array))
#ex4
array = np.random.randint(-10, 11, (10))
print(np.abs(array))
print(np.amin(array))
print(np.cos(array))
print(np.argmin(array))
print(np.log(array))
#ex5
array = np.random.randint(1, 10, (3, 5))
array.sort(axis=0)
print(array)
np.random.shuffle(array)
print(array)