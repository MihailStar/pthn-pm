# ⊗pyPmUFFN

# №1
def square(num):
    return num**2
def cube(num):
    return num**3
def func_1(num):
    print(cube(square(num)))

# №2
def func_2(unk):
    if isinstance(unk, str):
        return unk[0].upper() + unk[1:].lower()
    raise Exception()
def func_3(name):
    print("Hello", func_2(name))
