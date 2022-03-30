#Создать массив, который одинаково читается как слева направо, так и справа налево.

import random
n=10

ar=[0]*n


for i in range(n//2):
	ar[i]= random.randint(0, 10)
	ar[n-i-1] = ar[i]

print(ar)