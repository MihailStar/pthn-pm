# ⊗pyPmLpFI

# №1
tst = {-2, 1, 3, -5, 4, -8}
for number in tst:
    if number > 0:
        print(number)

# №2
tst = [7, 1, 2, 5, 3, 9]
result = []
for number in tst:
    if 2 < number < 5:
        result.append(number)
print(result)

# №3
tst = (1, 2, 3, 4, 5, 6, 7)
total = 0
for number in tst:
    if number % 2 == 0:
        total += number
print(total)

# №4
tst = 1234567
result = []
for digit in str(tst):
    number = int(digit)
    if number % 2 == 1:
        result.append(number)
print(result)
