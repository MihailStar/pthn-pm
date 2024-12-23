# ⊗pyPmLpSI

# №1
tst1 = [1, 3, 5]
tst2 = [2, 4, 6]
for item in zip(tst1, tst2):
    print(item)

# №2
tst1 = ["a", "b", "c"]
tst2 = ["d", "e", "f"]
result = []
for index, value in enumerate(tst1):
    result.append(value)
    result.append(str(index + 1))
print(result == ["a", "1", "b", "2", "c", "3"])

# №3
tst1 = [11, 12, 13, 14]
tst2 = [21, 22, 23, 24]
tst3 = [31, 32, 33, 34]
result = []
for item in zip(tst1, tst2, tst3):
    result += [sum(item)]
print(result == [11 + 21 + 31, 12 + 22 + 32, 13 + 23 + 33, 14 + 24 + 34])
