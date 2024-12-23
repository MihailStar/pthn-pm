# ⊗pyPmIBMP

# №1
from math import pow
num1 = 5
num2 = 4
print(pow(num1, num2))

# №2
from math import pow
dct = {2: 4, 3: 2, 5: 4}
print(tuple(map(lambda item: pow(item[0], item[1]), dct.items())) == (16.0, 9.0, 625.0))

# №3
from math import sqrt
num = 16
print(sqrt(16))

# №4
from math import sqrt
lst = [2, 3, 4]
print(sqrt(sum(lst)))
