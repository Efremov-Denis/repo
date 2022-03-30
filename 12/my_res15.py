#Найдите сумму чисел массива, которые стоят на нечетных местах 
#и при этом превосходят сумму крайних элементов массива
#(каждое число превосходит сумму крайних элементов массива).
import random

ar = []

for i in range(10):
	n = random.randint(0, 10)
	ar.append(n)

border_sum = ar[0] + ar[-1]
sum = 0

for i in range(len(ar)):
	if i % 2 != 0 and ar[i]>border_sum :
		sum += ar[i]

print(sum)

print(*ar)