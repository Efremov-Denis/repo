#Найти количество чисел в массиве, 
#которые делятся на 3, 
#но не делятся на 7.

import random

ar = []

for i in range(10):
	n = random.randint(0, 100)
	ar.append(n)

sum = 0

for el in ar:
	if el % 3 == 0 and el % 7 != 0:
		sum += 1

print(sum)
print(ar)