# ⊗pyPmLpWI

# №1
number = 100
while True:
    number /= 2
    if number < 10:
        break
print(number)

# №2
number = 100
divisors = []
divisor = 1
while divisor <= number:
    if number % divisor == 0:
        divisors.append(divisor)
    divisor += 1
print(divisors)
