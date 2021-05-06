import json
#
f = open('test2.txt', 'r')
data = json.load(f)
f.close()
n = 0
summ = 0
for key,value in data.items():
    if int(value) < 20000:
        print (f'Сотрудник с зп менее 20 000 {key}')
    n += 1
    summ += int(value)
summ = summ / n
print (f'Средняя зарплата: {summ}')