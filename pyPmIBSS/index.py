# ⊗pyPmIBSS

# №1
txt = "a/b/c/d"
print("a/b/c/d".split("/") == ["a", "b", "c", "d"])

# №2
txt = "a.b.c.d"
print(txt.rsplit(".", 1) == ["a.b.c", "d"])

# №3
txt = "ab%cd%"
print(txt.partition("%") == ("ab", "%", "cd%"))

# №4
txt = "2025-12-31"
print(txt.rpartition("-") == ("2025-12", "-", "31"))

# №5
txt = "2025-12-31"
print(txt.rpartition("-") == ("2025-12", "-", "31"))

# №6
lst = ["a", "b", "c", "d"]
print("".join(lst) == "abcd")

# №7
lst = ["2025", "31", "12"]
print("/".join(lst) == "2025/31/12")

# №8
lst = [1, 2, 3]
print("".join(map(str, lst)) == "123")
