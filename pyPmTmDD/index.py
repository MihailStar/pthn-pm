# ⊗pyPmTmDD

# №1
from datetime import datetime
dt1 = datetime.strptime("13/10/2018 22:15:45", "%d/%m/%Y %H:%M:%S")
dt2 = datetime.strptime("15/11/2018 09:47:16", "%d/%m/%Y %H:%M:%S")
print(dt2 - dt1)

# №2
from datetime import datetime
dt1 = datetime.strptime("01-12-2025 16:07:5", "%d-%m-%Y %H:%M:%S")
dt2 = datetime.strptime("31:12:2025 10:32:45", "%d:%m:%Y %H:%M:%S")
print(dt2 - dt1)
