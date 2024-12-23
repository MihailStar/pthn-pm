# ⊗pyPmCdOTCh

# №1
variable = 0
print("+++" if isinstance(variable, int) and not isinstance(variable, bool) else "---")

# №2
variable = 0.0
print("+++" if isinstance(variable, float) else "---")

# №3
variable = "0"
print("+++" if isinstance(variable, str) else "---")

# №4
variable = {0: 0}
print("+++" if isinstance(variable, dict) else "---")

# №5
variable = {0}
print("+++" if isinstance(variable, set) else "---")

# №6
variable = (0,)
print("+++" if isinstance(variable, tuple) else "---")

# №7
variable = [0]
print("+++" if isinstance(variable, list) else "---")
