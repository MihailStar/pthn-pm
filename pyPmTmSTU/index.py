# ⊗pyPmTmSTU

# №1
from time import gmtime, localtime
gm_time = gmtime()
curr_time = localtime()
print(gm_time.tm_hour, ":", gm_time.tm_min, sep="")
print(curr_time.tm_hour, ":", curr_time.tm_min, sep="")
