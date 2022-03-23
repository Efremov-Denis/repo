#Сформировать убывающий массив 
#из чисел, которые делятся на 3.

k = 6
my_list = []

for i in range(20):
	k -= 3
	my_list.append(k)

print(my_list)