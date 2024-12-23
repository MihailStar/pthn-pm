# ⊗pyPmCdEI

# №1
tst1 = 5
tst2 = 8
if tst1 > tst2:
    print("`tst1` больше `tst2`")
elif tst1 < tst2:
    print("`tst2` больше `tst1`")

# №2
age = 60
if 10 < age < 18:
    pass
elif 18 < age < 60:
    pass
else:
    print("Не попадает ни в одно из условий")

# №3
day = 15
if 1 <= day <= 10:
    print("1 декада")
elif 11 <= day <= 20:
    print("2 декада")
elif 21 <= day <= 31:
    print("3 декада")
else:
    raise Exception()
