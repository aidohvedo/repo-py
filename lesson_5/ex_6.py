import re

s = list()
f = open('ex_6.txt', 'r')
for line in f:
    s.append(line.split())
f.close()

n = 0
r = 0
slov = {}
while n <len(s):
    for i in s[n]:
        t = re.findall('(\d+)', i)
        t = ''.join(t)
        t.replace(' ', '')
        if t != '':
            r = r + int(t)
    slov[s[n][0]] = r
    r = 0
    n+=1

print (slov)
