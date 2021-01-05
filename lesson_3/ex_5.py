
def myfunc():
    b = 0
    r = 1
    while r == 1:
        a = list(input('Input numbers: ').split())
        for i in a:
            if i == 'q':
                return b
            b = b + int(i)
        a.clear()
        a = (b)
        print (a)

print (myfunc())