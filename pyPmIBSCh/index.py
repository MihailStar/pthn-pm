# ⊗pyPmIBSCh

# №1
txt = "Abcde"
print(txt.istitle())

# №2
lst = ["User1", "User2", "user3", "User4"]
print(all(map(lambda item: item.istitle(), lst)))

# №3
txt = "ABCDE"
print(txt.isupper())

# №4
txt = "abcde"
print(txt.islower())

# №5
txt = "abcde"
print(txt.isalpha())

# №6
txt = "12345"
print(txt.isdigit())

# №7
txt = "Ⅷ"
print(txt.isnumeric())

# №8
txt = "12345abc"
print(txt.isalnum())

# №9
txt = "a1b2c3d "
print(txt.rstrip().isalnum())

# №10
txt = " "
print(txt.isspace())

# №11
lst = ["a", "b", " ", "c", ""]
print(any(map(lambda char: char.isspace(), lst)))
