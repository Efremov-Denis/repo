#Создать массив, каждый элемент которого равен квадрату своего номера.

my_list = []
for i in range(10):
	my_list.append((i + 1)**2)

print(my_list)