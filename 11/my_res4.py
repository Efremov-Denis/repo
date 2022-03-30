#Сформировать массив из элементов арифметической прогрессии 
#с заданным первым элементом x 
#и разностью d.

x = int(input('Введите значение первого элемента'))
d = int(input('Введите значение разности прогрессии'))
sum = x
my_list = []

for i in range(x, x + 10):
	if i == x:
		my_list.append(i)
	else:
		sum += d
		my_list.append(sum)

print(my_list)