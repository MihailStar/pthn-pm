# ⊗pyPmDcKVG

# №1
dct = {"x": 3, "y": 2, "z": 1}
print(dct.items())

# №2
dct = {"a": [2, 4], "b": [3, 5]}
print(dct.items())

# №3
dct = {1: "x", 2: "y", 3: "z", 4: "w"}
print(list(dct.items()))

# №4
dct = {"a": 12, "b": 34, "c": 56}
result = []
for key, value in dct.items():
    result.append(key)
    result.append(value)
print(result == ["a", 12, "b", 34, "c", 56])
