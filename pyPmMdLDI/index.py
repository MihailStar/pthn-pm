# ⊗pyPmMdLDI

# №1
lst = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "b": 5, "c": 6},
    {"a": 7, "b": 8, "c": 9},
]
total = 0
for dct in lst:
    for value in dct.values():
        total += value
print(total)

# №2
for dct in lst:
    for key, value in dct.items():
        print(key, value)
