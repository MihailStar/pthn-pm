# ⊗pyPmStCOp

# №1
st1 = {1, 3, 6, 8}
st2 = {5, 8, 4, 2}
st3 = {4, 7, 3, 1}
print(st1.union(st2).intersection(st3))
print(st1.union(st3).intersection(st2))

# №2
st1 = {4, 2, 6, 10}
st2 = {1, 6, 3, 2}
st3 = {5, 8}
st4 = {6, 3, 1}
print(st1.difference(st2).intersection(st3.union(st4)))
