# ⊗pyPmLpDK

# №1
tst = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key in tst:
    print(key)

# №2
tst = {2: "a", 4: "b", 6: "c", 8: "d"}
for key in tst:
    if key == 8:
        continue
    print(key)

# №3
tst = {"1": "a", "2": "b", "3": "c", "4": "d"}
print(tuple(filter(lambda key: key != "1", tst.keys())) == ("2", "3", "4"))
