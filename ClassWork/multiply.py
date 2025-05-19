
def multiply(number1 , number2):
	result = 0
	if number2 < 0:
		for i in range(0, abs(number2)):

			result = result + number1

		return result
	elif number1 < 0:
		for product in range(0, abs(number2)):
			result = result + number1
		return result

	else: 
		for product in range (0, abs(number2)):
			result = result + number1
		return result

digit1 = float(input("Enter first number: "))
digit2 = int(input("Enter second number: "))

print(multiply(digit1,digit2))

