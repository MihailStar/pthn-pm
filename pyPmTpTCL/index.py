# ⊗pyPmTpTCL

# №1
tpl = ("2", "6", "12")
lst = list(tpl)

# №2
tpl1 = ("1", "2", "3")
tpl2 = ("4", "5")
print(list(tpl1) + list(tpl2) == ["1", "2", "3", "4", "5"])

# №3
tpl = (1, 2, 3, 4, 5)
print(tuple(reversed(tpl)) == (5, 4, 3, 2, 1))
