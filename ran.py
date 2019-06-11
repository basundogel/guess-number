import random
r = random.randint(1, 100)
while True:
	num = input('猜數字1~100選一個:')
	num = int(num) 
	if num == r:
		print('終於猜對了!')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
