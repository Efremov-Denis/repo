#Сгенерировать случайную серию из 15 чисел, 
#в которой ровно 3 единицы, остальные нули.

import random

a=b=c=0

while a==b or a==c or b==c:
	a = random.randint(1, 15)
	b = random.randint(1, 15)
	c = random.randint(1, 15)

for i in range(15):
	if i == a or i == b or i == c:
		print(1)
	else:
		print(0)