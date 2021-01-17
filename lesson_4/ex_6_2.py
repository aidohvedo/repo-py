from itertools import count,cycle

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


count = 0
for item in cycle(a):
    if count > 7:
        break
    print(item)
    count += 1

