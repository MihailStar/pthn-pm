# ⊗pyPmMdLI

# №1
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sub_lst in lst:
    for value in sub_lst:
        print(value)

# №2
lst = [[2, 4, 6], [3, 5, 7], [9, 12, 15]]
total = 0
for sub_lst in lst:
    for value in sub_lst:
        total += value
print(total)

# №3
lst = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
result = ""
for sub_lst in lst:
    for value in sub_lst:
        result += value
print(result)
