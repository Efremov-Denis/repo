#Создать массив, состоящий из троек подряд идущих одинаковых элементов.

my_list = []
c = 1

for i in range(12):
	my_list.append(c)
	if len(my_list) % 3 == 0:
		c += 1

print(my_list)