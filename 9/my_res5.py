#Компьютер загадывает число от 1 до 100. 
#У пользователя три попытки отгадать. 
#После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.

import random
import time
pc_n = random.randint(1, 100)
user_atempt = 'Введите ваше число'
c = 0

while True:
	user_s_go = int(input(user_atempt))
	c += 1
	if user_s_go == pc_n:
		print('Вы угадали')
		break
	if pc_n > user_s_go:
		print('Загаданное число больше')
		time.sleep(1)
	if pc_n < user_s_go:
		print('Загаданное число меньше')
		time.sleep(1)
	if c == 3 and pc_n != user_s_go:
		print('Вы проиграли')
		break