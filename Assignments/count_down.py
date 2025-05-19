integer = int(input("Enter an integer: "))

while integer < 1 :
	integer = int(input("Enter an integer: "))


for numbers in range (integer, 0, -1) :
	if numbers == 1:
		print("BLAST OFF!!")
	else: 
		print(numbers)
