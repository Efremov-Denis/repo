#Заполните массив случайным образом нулями, единицами и двойками так, 
#чтобы первая двойка в массиве встречалась раньше первой единицы, 
#количество единиц было в точности равно суммарному количеству нулей и двоек.

import random

ar = []

for i in range(5):
	n = random.randint(0, 2)
	if n == 1:
		ar.append(0)
	else:
		ar.append(n)

for i in range(len(ar) +1):
	ar.append(1)

random.shuffle(ar)
ar.insert(0,2)
print(ar)