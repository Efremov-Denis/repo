#Найдите сумму и произведение элементов массива.

import random

ar = []

for i in range(10):
	n = random.randint(1, 100)
	ar.append(n)

mult = 1

for el in ar:
	mult *= el

print('Сумма элементов массива: ', sum(ar))
print('Произведение элементов массива: ', mult)