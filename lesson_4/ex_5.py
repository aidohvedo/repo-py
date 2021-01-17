from functools import reduce

new_list = [el for el in range(100,1000) if el%2 == 0]
sum_all = reduce(lambda x,y: x + y, new_list)
print (sum_all)