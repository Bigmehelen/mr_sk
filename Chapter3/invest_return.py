principal = int(input("Enter the principal: "))

rate = int(input("Enter the rate: "))

rate_percent = rate / 100

for years in range (1,31):
	
	principal = principal * (1 + rate_percent)

	print(f"The amount of money you get in year {years} is {principal:,.2f}" )

	