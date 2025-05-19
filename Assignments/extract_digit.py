digit = int(input("Enter an integer: "))

sum_digit = 0

while digit != 0:

	newDigit = digit % 10

	sum_digit = sum_digit + newDigit

	digit = digit // 10

print(f"The sum of digit is {sum_digit}")

