#Заполнить массив заданной длины различными простыми числами. 

n = int(input('Введите длину массива'))
my_list = []
i = 2
while len(my_list) < n:
	sum = 0
	for j in range(2, i):
		if i % j == 0:
			sum += 1
	if sum == 0:
		my_list.append(i)
	i += 1

print(my_list)