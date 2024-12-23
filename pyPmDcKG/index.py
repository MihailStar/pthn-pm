# ⊗pyPmDcKG

# №1
dct = {"x": 1, "y": 2, "z": 3}
print(dct.keys())

# №2
dct = {1: "x", 2: "y", 3: "z", 4: "w"}
print(dct.keys())

# №3
dct = {"x": 1, "y": 2, "z": 3}
print(list(dct.keys()))

# №3
dct = {"x": 1, "y": 2, "z": 3}
print(list(dct))

# №4
from math import prod

dct = {2: "ab", 4: "cd", 6: "ef"}
print(prod(list(dct)))

# №5
dct = {1: "x", 2: "y", 3: "z", 4: "w"}
print(list(reversed(dct)) == [4, 3, 2, 1])
