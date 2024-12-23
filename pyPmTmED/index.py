# ⊗pyPmTmED

# №1
from time import mktime, strptime, time
dt = "24/07/2015 16:1"
start = mktime(strptime(dt, "%d/%m/%Y %H:%M"))
end = time()
print(end - start)

# №2
from time import mktime, strptime, time
dt1 = "12/02/23 10:12:54"
dt2 = "31/12/24 19:38:21"
start = mktime(strptime(dt1, "%d/%m/%y %H:%M:%S"))
end = mktime(strptime(dt2, "%d/%m/%y %H:%M:%S"))
print(end - start)

# №3
from math import ceil
seconds_in_day = 60 * 60 * 24
print(ceil((end - start) / seconds_in_day))
