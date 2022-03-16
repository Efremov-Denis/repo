#Реализуйте  "Камень, ножницы, бумага" с компьютером до трех побед

import random
import time

user_atempt = 'ваш ход'
l_comp =[
	'камень',
	'ножницы',
	'бумага'
]
victory = 0

while True:
	user_s_go = input(user_atempt)
	pc_go = random.choice(l_comp)
	print(pc_go)
	time.sleep(1)
	if user_s_go == 'камень' and pc_go == 'ножницы' or user_s_go == 'ножницы' and pc_go == 'бумага' or user_s_go == 'бумага' and pc_go == 'камень':
		victory += 1
	if victory == 3:
		print('Вы одержали три победы')
		break
'''
Замечания
1.
Долго вводить слова.  К тому же можно ошибиться, ввести например "Бумага" вместо "бумага".
Нужно привязать слова к цифрам, чтобы пользователь вводил: 1,2,3.
2.
Если компьютер побеждает 3 раза, игра должна останавливаться.