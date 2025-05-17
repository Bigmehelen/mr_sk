
def final_sum(numbers):

	sumOfNumber = 0
	
	while numbers != 0:

		newNumber = numbers % 10
		sumOfNumber = sumOfNumber + newNumber
		numbers = numbers // 10

	return sumOfNumber

numbers = int(input(" Enter a number: "))
print("Sum of number is ",final_sum(numbers))

	

