#Заполните массив случайным образом нулями и единицами так, 
#чтобы количество единиц было больше количества нулей.

import random

ar = [0]

while sum(ar) <= len(ar)//2:
	n = random.randint(0, 1)
	ar.append(n)

print(ar)