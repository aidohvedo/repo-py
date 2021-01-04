menu = 0
s =  0
num_bd = 1
a = []
sd = 0
while menu != '3':
    menu = input('Введите номер действия:')
    if menu == '2':
        d = input('Введите через пробел, название техники, стоимость, количество единиц и измерения(шт.)').split()
        a.insert(num_bd, ([num_bd, {'название':d[0], 'цена':d[1], 'количество':d[2], 'ед':d[3]}]))
        num_bd += 1
        print (a)
    elif menu == '1':
        print ('Показываю базу', a)
    elif menu == '4':
        print('Показываю аналитику')
        bd1 = []
        bd2 = []
        bd3 = []
        bd4 = []
        for m in a:
            #bd1 = list(a[s][1].values())
            bd1.append(a[s][1]['название'])
            bd2.append(a[s][1]['цена'])
            bd3.append(a[s][1]['количество'])
            bd4.append(a[s][1]['ед'])
            s += 1
        bd = {'название':bd1, 'цена':bd2, 'количество':bd3, 'ед':bd4}
        print (bd)


