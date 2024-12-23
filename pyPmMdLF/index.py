# ⊗pyPmMdLF

# №1
lst = []
for _ in range(3):
    nums = []
    for num in range(1, 4):
        nums.append(num)
    lst.append(nums)
print(lst == [[1, 2, 3], [1, 2, 3], [1, 2, 3]])

# №2
lst1 = []
lst2 = ["a", "b", "c"]
for _ in range(2):
    lst1.append(lst2)
print(lst1 == [["a", "b", "c"], ["a", "b", "c"]])
