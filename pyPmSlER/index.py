# ⊗pyPmSlER

# №1
lst = [1, 2, 3, 4, 5, 6]
del lst[1::2]

# №1
lst = [1, 2, 3, 4, 5, 6]
del lst[::2]

# №2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
del lst[-2::-2]
lst = lst[::-1]
print(lst == [8, 6, 4, 2])

# №2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst[::-2] == [8, 6, 4, 2])
