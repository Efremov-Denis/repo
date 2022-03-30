#Найдите сумму чисел массива, которые стоят на четных местах.

import random

ar = []
sum = 0

for i in range(10):
	n = random.randint(0, 12)
	ar.append(n)

for i in range(len(ar)):
	if i % 2 != 0:
		sum += ar[i]

print(sum)
print(ar)