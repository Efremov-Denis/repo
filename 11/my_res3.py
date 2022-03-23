#Заполнить массив последовательными нечетными числами, 
#начиная с единицы.

my_list = []

for i in range(1, 11):
	if i % 2 != 0:
		my_list.append(i)

print(my_list)