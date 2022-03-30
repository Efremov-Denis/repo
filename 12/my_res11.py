#Найдите сумму четных чисел массива.

import random

ar = []
sum = 0
for i in range(10):
	n = random.randint(0, 10)
	ar.append(n)

for el in ar:
	if el % 2 == 0:
		sum += 1

print('Сумма четных чисел массива равна: ', sum)