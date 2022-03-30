#Создайте массив, в котором количество отрицательных чисел равно количеству положительных 
#и положительные числа расположены на случайных местах в массиве.

import random

ar = []

for i in range(5):
	ar.append(random.randint(1, 9))
	ar.append(random.randint(-9, -1))

random.shuffle(ar)

print(ar)