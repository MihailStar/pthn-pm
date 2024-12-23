# ⊗pyPmDcRBK

# №1
dct = {"x": 1, "y": 2, "z": 3}
del dct["x"]

# №2
dct = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
del dct[2]
del dct[4]
print(dct == {1: "a", 3: "c", 5: "e"})
