import json

i = 0
saldo = 0
summ_med = 0
firms = {}
firms_av = list()

my_f = open("ex_7.txt", "r")
n = sum(1 for _ in my_f)
my_f.seek(0,0)
while i < n:
    content = my_f.readline().split()
    saldo = int(content[2]) - int(content[3])
    firms[content[0]] = saldo
    summ_med = summ_med + saldo
    i+=1
summ_med = summ_med/4
firms_av.append(firms)
firms_av.append(f'average_profit":{summ_med}')
my_f.close()
print (firms_av)

with open("firms_av.json", "w") as write_f:
    json.dump(firms_av, write_f)