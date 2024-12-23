# ⊗pyPmTmWG

# №1
from datetime import date
current_date = date.today()
print(current_date.weekday())

# №2
if current_date.weekday() in (5, 6):
    print("Выходной")
else:
    print("Будний")

# №3
from datetime import date
d = date(2026, 11, 2)
print(d.weekday())
print(d.isoweekday())
