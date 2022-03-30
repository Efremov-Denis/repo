#Сформировать массив из случайных чисел, 
#в котором ровно две единицы, стоящие на случайных позициях.

import random

a = b = 0
my_list = []

while a == b:
	a = random.randint(0, 9)
	b = random.randint(0, 9)


for i in range(10):
	if i == a or i == b:
		my_list.append(1)
	else:
		c = 1
		while c == 1:
			c = random.randint(0, 9)
		my_list.append(c)

print(my_list)