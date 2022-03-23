#Заполнить массив нулями, 
#кроме первого и последнего элементов, которые должны быть равны единице.

my_list = []

for i in range(10):
	i = 0
	my_list.append(i)

my_list[0], my_list[-1] = 1, 1
print(my_list)