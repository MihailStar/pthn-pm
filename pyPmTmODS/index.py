# ⊗pyPmTmODS

# №1
from time import sleep
sleep(1.5)
print("Имя")

# №2
from time import sleep
lst = ["a", "b", "c", "d"]
for index, item in enumerate(lst):
    print(item)
    if index < len(lst) - 1:
        sleep(3)
