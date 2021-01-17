from sys import argv

stavka = {'Слесарь': '550', 'Монтер': '200','Водоопроводчик': '500'}
scriptname, doljnost, hours = argv
hours = int(hours)
cost = int(stavka[doljnost])
zp = cost * hours
print ('Ваша зарплата', zp, ' руб')


