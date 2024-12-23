# ⊗pyPmDcEBK

# №1
dct = {"x": 1, "y": 2, "z": 3}
dct.pop("x")

# №4
dct = {1: "ab", 2: "cd", 3: "ef"}
del dct[2]
print(list(dct.items()) == [(1, "ab"), (3, "ef")])
