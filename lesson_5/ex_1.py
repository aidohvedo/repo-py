s = 1
while s:
    s = input('Input text:')
    f = open('test.txt', 'a')
    f.write(s)
    f.close()
#