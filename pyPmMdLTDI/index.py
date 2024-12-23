# ⊗pyPmMdLTDI

# №1
lst = [
    [["q", "w", "e"], ["r", "t", "y"], ["u", "i", "o"]],
    [["p", "a", "s"], ["d", "f", "g"], ["h", "j", "k"]],
    [["l", "z", "x"], ["c", "v", "b"], ["n", "m", "q"]],
]
for z in lst:
    for y in z:
        for x in y:
            print(x, end=" ")
        print()

# №2
lst = [
    [[1, 3], [5, 7]],
    [[2, 4], [6, 8]],
]
total = 0
for z in lst:
    for y in z:
        for x in y:
            total += x
print(total)
