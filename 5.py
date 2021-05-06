
#a = input('Введите слова через пробел: ')
s = 3
a = [1,5,5,6,2]
n = 0
ind =0

for i in a:
    if i == s:
        ind = n
    n+=1

#test
if bool(ind):
    a.insert(ind, s)
else:
    a.append(s)

print (a)
