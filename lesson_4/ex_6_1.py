from sys import argv
import random

scriptname, num = argv
num = int(num)
while True:
    s = random.randint(num,10)
    print (s)
    if s == 10:
        break

