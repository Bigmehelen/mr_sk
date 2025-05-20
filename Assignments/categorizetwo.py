def get_categorize(*numbers):

	divisibles = ()

	count = 0
	while count < len(numbers):

		if numbers[count] % 5 == 0:
			divisibles = divisibles + (numbers[count],)
		count+=1

	if divisibles:
		return list(divisibles)
	else:
		return('No divisible numbers found')
	
print(get_categorize(10,15,21,30,45))		