# ⊗pyPmLpLEC

# №1
lst = [2, 4, 8]
if all(map(lambda number: number % 2 == 0, lst)):
    print("+++")
else:
    print("---")

# №2
tst = "abcdef"
for char in tst:
    if char == "d":
        print("+++")
        break
else:
    print("---")
