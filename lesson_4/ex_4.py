from itertools import groupby

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = list()
#b = [el for el, _ in groupby(a)]
#b = list(set(a))

n = []
for i in a:
    if i not in n:
        n.append(i)

b = [el for el in n]

print (b)
