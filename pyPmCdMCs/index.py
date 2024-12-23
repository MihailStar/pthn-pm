# ⊗pyPmCdMCs

# №1
num = 3
match num:
    case 1:
        print("Зима")
    case 2:
        print("Весна")
    case 3:
        print("Лето")
    case 4:
        print("Осень")
    case _:
        raise Exception()

# №2
month = 6
match month:
    case 12 | 1 | 2:
        print("Зима")
    case 3 | 4 | 5:
        print("Весна")
    case 6 | 7 | 8:
        print("Лето")
    case 9 | 10 | 11:
        print("Осень")
    case _:
        raise Exception()

# №3
tst = True
match tst:
    case str():
        print("`tst` is string")
    case int() | float() as numOrBool if type(numOrBool) != bool:
        print("`tst` is number")
    case _:
        print("`tst` is not string or number")
