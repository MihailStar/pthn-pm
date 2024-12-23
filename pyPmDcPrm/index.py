# ⊗pyPmDcPrm

# №1
dct = {"x": "1", "y": "2", "z": "3"}
print(sum(map(lambda value: int(value) ** 2, dct.values())))

# №1
from functools import reduce

dct = {"x": "1", "y": "2", "z": "3"}
print(reduce(lambda acc, value: acc + int(value) ** 2, dct.values(), 0))

# №2
dct1 = {"1": 12, "2": 24, "3": 36}
dct2 = {"a": "3", "b": "6", "c": "9"}
sum1 = sum(dct1.values())
sum2 = sum(map(lambda value: int(value), dct2.values()))
print(sum1 - sum2)

# №3
dct = {1: "4", 2: "5", 3: "6"}
print(dict(map(lambda item: (str(item[0]), item[1]), dct.items())))

# №4
dct = {"x": "1", "y": "2", "z": "3"}
print(
    list(map(lambda item: item[1] * item[0], enumerate(dct.values(), 2)))
    == ["11", "222", "3333"]
)

# №5
dct = {"x": 1, "y": 2, "z": 3}
print("".join(map(lambda value: str(value), dct.values())) == "123")

# №6
dct = {"a": 7, "b": 6, "c": 5}
print("/".join(map(lambda value: str(value), reversed(dct.values()))) == "5/6/7")

# №7
dct = {"y": 2025, "m": 12, "d": 31}
print("-".join(map(lambda value: str(value), dct.values())) == "2025-12-31")
