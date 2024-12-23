# ⊗pyPmIBMRa

# №1
from random import randint

num1 = 10
num2 = 20
print(randint(num1, num2))

# №2
from random import randint

num1 = 5
num2 = 30
print(randint(num1, num2))

# №3
from random import uniform

num1 = 1.345
num2 = 14.784
print(uniform(num1, num2))

# №4
from random import uniform

num1 = -2
num2 = 10
print(uniform(num1, num2))

# №5
from random import randrange

num1 = 5
num2 = 50
num3 = 4
print(randrange(num1, num2, num3))

# №6
from random import choice

lst = [1, 2, 3, 4, 5]
print(choice(lst))

# №7
from random import sample

lst = [1, 2, 3, 4, 5]
print(sample(lst, 3))

# №8
from random import shuffle

lst = [1, 2, 3, 4, 5]
shuffle(lst)
print(lst)

# №9
lst = [1, 1, 1, 2, 2, 3, 3, 4, 5]
print(sample(list(set(lst)), 3))

# №10
from random import seed

num = 7
seed(num)

# №11
from random import seed

tlp = (10, 6, 2, 4)
seed((choice(tlp)))
