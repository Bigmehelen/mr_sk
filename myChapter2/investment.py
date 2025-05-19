
principal = 1000
rate = 7 / 100
amount = 0;

for years in range(10 , 40 , 10):
	noOfYears = int(input("Enter the years: "))
	amount = principal * (1 + rate)**noOfYears
	print("The amount at the end of the year is: %2d" %amount)