# ⊗pyPmLpRLA

# №1
tst = [1, 2, 3, 4, 5]
total = 0
for number in tst:
    total += number**2
print(total)

# №2
tst = ["a", "b", "c", "d", "e"]
result = ""
for char in tst:
    result += char
print(result == "abcde")

# №3
tst = [1, 2, 3, 4, 5]
result = ""
for number in tst:
    result += str(number)
print(int(result) == 12345)
