# ⊗pyPmTmLY

# №1
from calendar import isleap
year = 2020
print(("" if isleap(year) else "не") + "високосный")

# №2
from calendar import isleap
year = 1910
if isleap(year):
    print("+++")
else:
    print("---")

# №3
from calendar import isleap
from datetime import date
current_date = date.today()
if isleap(current_date.year):
    print("+++")
else:
    print("---")
