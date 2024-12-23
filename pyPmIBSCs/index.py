# ⊗pyPmIBSCs

# №1
txt = "ABCDE"
print(txt.lower())

# №2
txt = "abcde"
print(txt.upper())

# №3
txt = "abcde"
print(txt.capitalize())

# №4
txt = "word1 word2 word3"
print(txt.title())

# №5
txt = "ABC def"
print(txt.swapcase())

# №6
lst = list(map(lambda word: word.capitalize(), ["ab", "Cd", "eF"]))
print(lst)

# №7
dct = {"user_1": "User_1@Domen", "user_2": "User_2@Domen"}
for key in dct:
    dct[key] = dct[key].lower()
print(dct)
