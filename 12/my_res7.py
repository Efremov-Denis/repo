#Найти количество четных чисел в массиве.

import random

ar = []

for i in range(20):
	n = random.randint(0, 100)
	ar.append(n)

sum = 0

for el in ar:
	if el % 2 == 0:
		sum += 1

print('Количество четных чисел в массиве ar =: ', sum)