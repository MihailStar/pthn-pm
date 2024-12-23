# ⊗pyPmLpDV

# №1
tst = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key in tst:
    value = tst[key]
    print(value)

# №2
tst = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(sum(tst.values()))

# №3
from functools import reduce

tst = {"1": "a", "2": "b", "3": "c", "4": "d"}
print(reduce(lambda result, value: result + value, tst.values(), ""))
