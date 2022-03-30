#Сформировать массив из случайных целых чисел от 0 до 9 , 
#в котором единиц от 3 до 5 
#и двоек больше троек.

import random

d = random.randint(3, 5)
ar1 = [1]*d

for i in range(d):
	n = random.randint(0, 9)
	ar1.append(n)

s_2 = 0
s_3 = 0
ar2 = [2,3]

while s_3 >= s_2:
	n = random.randint(2, 3)
	ar2.append(n)
	if n == 2:
		s_2 += 1
	if n == 3:
		s_3 += 1

for i in range(len(ar2)):
	ar1.append(ar2[i])

random.shuffle(ar1)
print(ar1)