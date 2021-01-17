def fac(n):
    n += 1
    s = 1
    f = 1
    while s != n:
        f = f * s
        s += 1
        yield f

#fac2 = fac(4)
#print(fac2)

for el in fac(4):
    print(el)