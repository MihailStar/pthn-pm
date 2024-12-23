# ⊗pyPmUFPrm

# №1
def func_1(first_name, last_name, course):
    print(last_name.upper(), first_name.capitalize(), course)

# №2
def func_2(side_a, side_b):
    print(side_a * side_b)

# №3
def func_3(string):
    return tuple(string)

# №4
def func_4(number_a, number_b):
    if number_a > number_b:
        print(number_a, "больше", number_b)
    elif number_a < number_b:
        print(number_b, "больше", number_a)
    else:
        print(number_a, "равно", number_b)

# №5
def func_5(variable):
    if isinstance(variable, (int, float)) and not isinstance(variable, bool):
        str(variable)
    return variable

# №6
def func_6(stop):
    start = 1
    result = []
    for number in range(start, stop + 1):
        if number % 2 == 0:
            result.append(number)
    return result

# №7
def func_7(user_to_age):
    return tuple(user_to_age.items())

# №8
def func_8(day_of_week):
    match day_of_week:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            raise Exception()
