# ⊗pyPmStPrm

# №1
st1 = {"x", "1", "y", "2", "z"}
st2 = {1, 2, 3, 4, 5, 6}
print("st1" if len(st1) > len(st2) else "st2")

# №2
num1 = 12345
num2 = 12321
print("+++" if set(str(num2)).issubset(set(str(num1))) else "---")

# №3
tst1 = 34
tst2 = [1, 2, 5]
tst3 = (6, 7, 8)
st = set()
st.add(tst1)
st.update(tst2, tst3)

# №4
st = {"18", "24", "34", "47", "81", "63"}
tst1 = "34"
tst2 = ("81", "12", "46")
print("+++" if tst1 in st else "---")
print("+++" if set(tst2).issubset(st) else "---")

# №5
num1 = 12345
num2 = 45123
print("+++" if set(str(num1)) == set(str(num2)) else "---")

# №6
num1 = 12345
num2 = 45678
common_digits = set(str(num1)).intersection(set(str(num2)))
print("".join(common_digits))

# №7
st1 = {"ab", "b", "ce", "de", "d"}
st2 = {"ef", "d", "ab", "bc"}
st3 = {"a", "g", "b", "c"}
print(st1.intersection(st2).union(st3))
