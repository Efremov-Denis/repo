#Создать массив из n первых чисел Фибоначчи.

n = int(input('Введите число'))
fib1 = 1
fib2 = 1
i = 0
my_list = [1,1]

while i < n - 2:
	sum = fib1 + fib2
	fib1 = fib2
	fib2 = sum
	my_list.append(sum)
	i += 1
if n == 1:
	my_list = [1]

print(my_list)



import random

ar = [0]*10
ar[0]=0
ar[1]=1

for i in range(2, 10):
	ar[i]= ar[i-1]+ ar[i-2]
	

print(*ar)