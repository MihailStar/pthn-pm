# ⊗pyPmLpDI

# №1
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(*dct.items(), sep="\n")

# №2
dct = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}
for key, name in dct.items():
    print({"key": key, "value": name})
