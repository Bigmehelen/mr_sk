"""
1. prompt the user to input amount to borrow
2. cast the amount to borrow to a float
3. prompt the user to input the annual interest rate 
4. cast the annual interest rate to a float
5. prompt the user to input the number of months in a year
6. cast the number of months to a float
7. make percentage value a decimal by dividing by 100 and divide by 12 number of month in a year
8. multiply the number of months in duration by number of month in a year
9. the first formula is monthly interest rate multipy by (1 + monthly interest rate) raised to the power of the number of months
10. second formula is (1 + monthly interest rate ) raised to the power of number of month - 1
11. multiply amount by the first first formula and divide by second formula
12. print result
""" 
amount = float(input("Enter amount to borrow: "))
air = float(input("Enter the annual interest rate: "))
month = float(input("Enter number of months in years: "))

rate = (air / 100) / 12
nm = month * 12
mr = rate * (1 + rate)**nm
mr2 = (1 + rate)**nm -1
mp = amount * mr / mr2
	
print("monthly payment is $ %.2f" %mp)