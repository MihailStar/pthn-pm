# ⊗pyPmLpBr

# №1
tst = {1, 3, 6, 7, -9, 12}
for number in tst:
    if number < 0:
        break
    print(number)

# №2
tst = [7, 1, 2, 5, 0, 3, 9]
total = 0
for number in tst:
    if number == 0:
        break
    total += number
print(total)

# №3
tst = 897654
result = []
for digit in str(tst):
    if digit == "6":
        break
    result.append(int(digit))
print(result)
