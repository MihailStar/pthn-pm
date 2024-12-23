# ⊗pyPmDcCo

# №1
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"x": 4, "y": 5, "z": 6}
dct = {}
dct.update(dct1)
dct.update(dct2)

# №2
dct1 = {"3": "c", "4": "d", "5": "e"}
dct2 = {"1": "a", "2": "b"}
dct2.update(dct1)
print(dct2 == {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e"})

# №3
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"x": 4, "y": 5, "z": 6}
dct1.update(dct2)
print(list(dct.values()))

# №4
dct1 = {"a": 1, "b": 2, "c": 3}
dct2 = {"d": 4, "e": 5, "f": 6}
dct3 = {"j": 7, "h": 8, "i": 9}
dct = {}
dct.update(dct1)
dct.update(dct2)
dct.update(dct3)
