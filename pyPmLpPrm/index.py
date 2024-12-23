# ⊗pyPmLpPrm

# №1
tst = {"1": "a", "2": "b", "3": "c", "4": "d"}
result = []
for index, key in enumerate(tst):
    if index == 3:
        break
    result.append(index)
    result.append(tst[key])
print(result == [0, "a", 1, "b", 2, "c"])

# №1
tst = {"1": "a", "2": "b", "3": "c", "4": "d"}
result = []
for index, value in enumerate(tst.values()):
    if index == 3:
        break
    result.extend((index, value))
print(result == [0, "a", 1, "b", 2, "c"])

# №2
result = ""
for number in range(2, 21, 2):
    result += str(number)
print(result)

# №3
for number in range(99, 0, -2):
    print(number)

# №4
result = []
for _ in range(10):
    result.append("x")
print(result)

# №5
result = set()
for i in range(10):
    result.add(chr(ord("a") + i))
print(result)

# №6
tpl = (13, 11, 9, 7, 5, 3)
for number in tpl:
    if 10 > number > 5:
        print(number)

# №7
string = "bfejdichga"
for char in string:
    if char == "c":
        print("+++")
        break
else:
    print("---")

# №8
lst = [13, 11, 9, 7, 5, 3]
total = 0
for number in lst:
    total += number
print(total / len(lst))

# №9
lst = [-13, -11, 9, 7, -5, -3]
for number in lst:
    if number > 0:
        break
    print(number)

# №10
users = [
    {"first_name": "Name1", "last_name": "", "age": 0},
    {"first_name": "name2", "last_name": "", "age": 0},
    {"first_name": "NAME3", "last_name": "", "age": 0},
    {"first_name": "name4", "last_name": "", "age": 0},
    {"first_name": "Name5", "last_name": "", "age": 0},
]
for user in users:
    for item in user.items():
        print(item, end="")
    print()

# №10
dct = {
    "user1": {"first_name": "Name1", "last_name": "", "age": 0},
    "user2": {"first_name": "name2", "last_name": "", "age": 0},
    "user3": {"first_name": "NAME3", "last_name": "", "age": 0},
    "user4": {"first_name": "name4", "last_name": "", "age": 0},
    "user5": {"first_name": "Name5", "last_name": "", "age": 0},
}
for user_info in dct.values():
    for item in user_info.items():
        print(item, end="")
    print()

# №11
for user in users:
    print(user["first_name"][0].upper() + user["first_name"][1:].lower())

# №11
for user_info in dct.values():
    print(user_info["first_name"][0].upper() + user_info["first_name"][1:].lower())
