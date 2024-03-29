strs = ['1', '2', '3', '4', '5', '6', '7']

nums = []
i = 0
while i<len(strs):
    n = int(strs[i])
    nums.append(n)
    i += 1
    
# SELECT name FROM users WHERE id > 21
# Not 100% Declarative
for s in strs:
    n = int(s)
    nums.append(n)

# 100% Declarative
nums = map(lambda s: int(s), strs)
nums
tens = tuple(map(lambda n: n*10, nums))
tens
nums = [6, 3, 7, 2, 6, 9]
filtered = set(filter(lambda n: n>5, nums))
filtered

from functools import reduce

total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
total

total = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 10)
total

# https://projecteuler.net/archives
# 1, 6, 8, 9
