#Определить, содержит ли массив данное число x

import random

ar = []

for i in range(20):
	n = random.randint(0, 10)
	ar.append(n)

print(8 in ar)
print(ar)