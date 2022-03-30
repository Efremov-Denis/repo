#Определите, каких чисел в массиве больше: 
#которые делятся на первый элемент массива или которые делятся на последний элемент массива.

import random

ar = []

for i in range(10):
	n = random.randint(1, 100)
	ar.append(n)

sum_first = 0
sum_last = 0
first_el = ar[0]
last_el = ar[-1]

for el in ar:
	if el % first_el == 0:
		sum_first += 1
	if el % last_el == 0:
		sum_last += 1

if sum_first > sum_last:
	print('В массиве больше чисел, которые делятся на первый элемент массива')
elif sum_last > sum_first:
	print('В массиве больше чисел, которые делятся на последний элемент массива')
else:
	print('Массив содержит одинаковое количество чисел, которые делятся на его первый и последний элементы')