# ⊗pyPmLpFl

# №1
lst = [1, 2, 3, -4, 5]
is_all_positive = all(map(lambda number: number > 0, lst))
if is_all_positive:
    print("+++")
else:
    print("---")

# №2
number = 10
is_prime_number = True
for i in range(2, number):
    if number % i == 0:
        is_prime_number = False
        break
if is_prime_number:
    print("+++")
else:
    print("---")
