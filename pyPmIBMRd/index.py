# ⊗pyPmIBMRd

# №1
num = 16.456
print(round(num))

# №2
num = 21.167
print(round(num, 2))

# №3
from math import ceil
num = 3.348
print(ceil(num))

# №4
from math import floor
num = 18.565
print(floor(num))

# №5
from math import sqrt
num = 17
print(round(sqrt(num), 2))

# №6
from math import ceil, pow
num = 17
print(ceil(pow(num, 1 / 3)))

# №7
lst = [3.45, 1.54, 5.76]
print(list(map(round, lst)))

# №8
lst1 = [1.514, 4.897, 2.657]
lst2 = list(map(floor, lst1))
print(lst2 == [1, 4, 2])
