#Заполнить массив нулями и единицами, 
#при этом данные значения чередуются, начиная с нуля.

my_list = []

for i in range(10):
	if i % 2 == 0:
		i = 0
	else:
		i = 1
	my_list.append(i)

print(my_list)