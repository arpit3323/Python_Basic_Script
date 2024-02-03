def divisible_by_sum(number):

	st = str(number)
	sum = 0
	length = len(st)
	
	for i in st:
		sum = sum + int(i)
		

	if (number % sum == 0):
		return True
	else:
		return False



number = 123
print(divisible_by_sum(number))

