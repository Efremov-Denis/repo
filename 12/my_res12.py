#Найдите сумму нечетных чисел массива, 
#которые не превосходят 11.

import random

ar = []
sum = 0
for i in range(10):
	n = random.randint(0, 50)
	ar.append(n)

for el in ar:
	if el % 2 != 0 and el <= 11:
		sum += 1

print(sum)