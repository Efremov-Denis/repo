#Реализуйте  "Камень, ножницы, бумага" с компьютером до трех побед

import random
import time

user_atempt = 'ваш ход'
l_comp =[
	'камень',
	'ножницы',
	'бумага'
]
user_victory = 0
pc_victory = 0
print('Введите один из трех вариантов:\n1 - камень, 2 - ножницы, 3 - бумага')

while True:
	user_s_go = input(user_atempt)
	pc_go = random.choice(l_comp)
	print(pc_go)
	time.sleep(1)
	if user_s_go == '1' and pc_go == 'ножницы' or user_s_go == '2' and pc_go == 'бумага' or user_s_go == '3' and pc_go == 'камень':
		user_victory += 1
	elif pc_go == 'камень' and user_s_go == '2' or pc_go == 'ножницы' and user_s_go == '3' or pc_go == 'бумага' and pc_go == '1':
		pc_victory += 1
	else:
		user_victory += 0
		pc_victory += 0
	if user_victory == 3:
		print('Вы одержали три победы')
		break
	if pc_victory == 3:
		print('Компьютер одержал три победы')
		break