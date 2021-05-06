#

f = open('ex_5.txt', 'w')
new_list = [str(el) for el in range(1,10)]
f.writelines(new_list)
f.close()

f = open('ex_5.txt', 'r')
s = list(f.read())
f.close()
n = 0 
for i in s:
    n += int(i)
print (n)
