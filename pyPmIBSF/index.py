# ⊗pyPmIBSF

# №1
txt = "a1bc11de"
print(list(txt.replace("1", "").rstrip("e")) == ["a", "b", "c", "d"])

# №2
txt = " abcde "
print(txt.strip() == "abcde")

# №3
txt = " abcde "
print(txt.lstrip() == "abcde ")

# №4
txt = " abcde "
print(txt.rstrip() == " abcde")

# №5
txt = " abcde "
print(txt.rstrip() == " abcde")

# №6
txt = "abc {}"
num = 12
print(txt.format(num))

# №7
user_info = "user_1 {age}"
age = 33
print(user_info.format(age=age))

# №8
txt = ""
num = 6
print(txt.zfill(num) == "000000")

# №9
txt = "abcde"
print(txt.ljust(len(txt) + 3, "1") == "abcde111")

# №10
txt = "12345"
print(txt.rjust(len(txt) + 2, "a") == "aa12345")
