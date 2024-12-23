# ⊗pyPmIBSSe

# №1
txt = "abcdef"
print(txt.startswith("ac"))

# №2
lst = ["12", "13", "14", "15"]
print(all(map(lambda item: item.startswith("1"), lst)))

# №3
num = 123456
print(str(num).endswith("6"))

# №3
num = 123456
print(num % 10 == 6)

# №4
txt = "abcdef"
print(txt.index("c"))

# №5
txt = "ab1cd1ef"
print(txt.index("1", 3, 7))

# №6
txt = "123453637"
print(txt.rindex("3"))

# №7
txt = "2025.12.31"
print(txt.rindex("2"))

# №8
num = 24536589
print(str(num).count("5"))

# №9
lst = ["abc", "cde", "cbb", "aeb"]
print(list(map(lambda string: string.count("b"), lst)))

# №10
txt = "http1://code.mu"
print(txt.replace("1", "s") == "https://code.mu")

# №11
txt = "a.bc.d.ef"
print(txt.replace(".", " "))
