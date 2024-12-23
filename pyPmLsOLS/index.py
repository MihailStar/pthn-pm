# ⊗pyPmLsOLS

# №1
lst = [4, 2, 5, 1, 3]
lst.sort(reverse=False)

# №2
lst = [4, 2, 5, 1, 3]
lst.sort(reverse=True)

# №3
lst = [1, 2, 3, 4, 5]
lst.sort(reverse=True)

# №4
lst1 = ["a", "b", "c"]
lst2 = [3, 2, 1]
lst1.sort(reverse=True)
lst2.sort()
print(lst2 + lst1 == [1, 2, 3, "c", "b", "a"])

# №4
lst1 = ["a", "b", "c"]
lst2 = [3, 2, 1]
lst1.reverse()
lst2.reverse()
print(lst2 + lst1 == [1, 2, 3, "c", "b", "a"])
