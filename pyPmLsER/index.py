# ⊗pyPmLsER

# №3
lst1 = [1, 2, 3, 4]
lst2 = [7, 6, 5]

lst2.append(lst1.pop(lst1.index(3)))
lst2.reverse()

lst1.append(lst2.pop(lst2.index(6)))
lst1.extend(lst2)

lst2.clear()

print(lst1 == [1, 2, 4, 6, 3, 5, 7])
