x = input('請輸入猜數字範圍最小值:')
x = int(x)
y = input('請輸入猜數字範圍最大值:')
y = int(y)
import random
r = random.randint(x, y)
count = 0
while True:
	count += 1	
	num = input('請猜數字:')
	num = int(num) 
	if num == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次')
			
