# ⊗pyPmLpCn

# №1
tst = {"a", "b", "c", "d", "e"}
for char in tst:
    if char == "d":
        continue
    print(char)

# №2
tst = [6, 3, -2, 8, -4, 9]
for num in tst:
    if num < 0:
        continue
    print(num)

# №3
tst = ["a", "b", "c", "d", "e"]
result = ""
for char in tst:
    if char == "b":
        continue
    result += char
print(result == "acde")
