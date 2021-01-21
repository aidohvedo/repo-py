i = 0
f = open('test1.txt', 'r')
s = list(f.readlines())
f.close()

print (f'Кол-во строк - {len(s)}')

while i < len(s):
    r = s[i].split()
    i +=1
#    t = str(len(r))[-1]

    if int(len(r)) > 10:
        t = str(len(r))[-2:]
    else:
        t = str(len(r))[-1]
    if t in ('2','3','4'):
        oko = 'a'
    elif t in ('5','6','7','8','9','0','11','12','13','14'):
        oko = ''
    else:
        oko = 'о'

    print (f'В строке {i} - {len(r)} слов{oko}')

