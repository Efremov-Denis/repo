#Сгенерировать случайную серию из 15 чисел, 
#в которой ровно 3 единицы, остальные нули.

import random

random_list = []
for i in range(15):
	random_list.append(random.randint(0, 1))
sum = 0
for el in random_list:
	if el == 1:
		sum += 1
	if sum > 3:
		el = 0
	print(el)

import random

i = 0
sum = 0

while i < 15:
	n = random.randint(0, 1)
	if n == 1:
		sum += 1
	if sum > 3:
		n = 0
	print(n)
	i+=1
'''
Замечания
1.
согласно теории вероятности, в моем алгоритме единички будут выпадать ближе к началу.
Хочется размазать их по всей цепочке.
2.
могут выпасть только две единички.