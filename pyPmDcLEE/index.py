# ⊗pyPmDcLEE

# №1
dct = {"x": 1, "y": 2, "z": 3}
print(dct.popitem())

# №2
dct = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
dct.popitem()
print(list(reversed(dct.keys())) == [4, 3, 2, 1])
