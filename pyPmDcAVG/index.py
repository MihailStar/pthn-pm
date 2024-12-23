# ⊗pyPmDcAVG

# №1
dct = {"x": 1, "y": 2, "z": 3}
print(dct.values())

# №2
dct = {4: "x", 2: "y", 3: "z", 4: "w"}
print(dct.values())

# №3
dct = {"x": 1, "y": 2, "z": 3}
print(list(dct.values()))

# №4
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {1: "a", 2: "b", 3: "c"}
print(list(dct1.values()) + list(dct2.values()) == [1, 2, 3, "a", "b", "c"])
