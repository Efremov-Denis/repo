#Сформировать возрастающий массив из четных чисел.

my_list = []

for i in range(11):
	if i % 2 == 0:
		my_list.append(i)

print(my_list)