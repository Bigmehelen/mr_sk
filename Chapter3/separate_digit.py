number = int(input("Enter a five digit number: "))

divisor = 10_000

while number != 0:

	digit = number // divisor

	print(digit, end= "\t")

	number = number % divisor

	divisor = divisor // 10