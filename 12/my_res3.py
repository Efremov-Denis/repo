#Создайте массив, в котором количество отрицательных чисел равно количеству положительных 
#и положительные числа расположены на случайных местах в массиве.

import random

ar1 = []

for i in range(5):
	n = random.randint(1, 9)
	ar1.append(n)

ar2 = ar1[::-1]
ar3 = []

for el in ar2:
	ar3.append(-el)

ar4 = []

for el in ar1:
	ar4.append(ar1[i])

for el in ar3:
	ar4.append(el)

random.shuffle(ar4)
print(ar4)