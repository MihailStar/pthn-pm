# ⊗pyPmLpEIG

# №1
tst = [8, 6, -4, 2, -1]
for index, num in enumerate(tst):
    if num < 0:
        break
    print({"value": num, "index": index})

# №2
tst = ["a", "b", "c", "d", "e"]
for index, char in enumerate(tst):
    print(char + str(index + 1))

# №3
tst = [1, 2, 3, 4, 5]
result = []
for index, num in enumerate(tst):
    result.append(num**2 if index % 2 == 0 else num**3)
print(result)
