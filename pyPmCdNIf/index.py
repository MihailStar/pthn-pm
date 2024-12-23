# ⊗pyPmCdNIf

# №1
month = 6
if 1 <= month <= 12:
    if month in (12, 1, 2):
        print("Зима")
    elif month in (3, 4, 5):
        print("Весна")
    elif month in (6, 7, 8):
        print("Лето")
    else:
        print("Осень")
else:
    raise Exception()

# №2
num = 60
if 10 <= num <= 99:
    if (num // 10) + (num % 10) <= 9:
        print("Сумма цифр однозначная")
    else:
        print("Сумма цифр двухзначная")
