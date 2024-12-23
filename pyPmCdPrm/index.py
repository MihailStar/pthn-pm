# ⊗pyPmCdPrm

# №1
variable = 222
if variable % 2 == 0:
    print("even")
else:
    print("odd")

# №2
variable = "2a2"
if "a" in variable:
    index_a = variable.index("a")
    print(variable[:index_a] + "!" + variable[index_a + 1:])

# №3
inputed = input()
if "@" not in inputed:
    inputed = input()

# №4
variable = "username"
if len(variable) < 3:
    print("short")
elif len(variable) > 20:
    print("long")
else:
    print("correct")

# №5
variable = "password"
if variable and 6 <= len(variable) <= 14:
    print("correct")
else:
    print("not correct")

# №6
tst = "abcdef"
print("string is too long" if len(tst) > 20 else "string is too short")
