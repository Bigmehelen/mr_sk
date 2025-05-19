total = 0
miles_per_gallon = 0
count = 0

miles = float(input("Enter amount of miles driven or -1 to end: "))
while miles != -1:
	if miles == -1:  
		break
	gallon = float(input("Enter amount of gallon used: "))
	if gallon == -1:
		break
	else:
		miles_per_gallon = miles / gallon
		total = total + miles_per_gallon
		print("The miles per gallon for this tank is %.2f" %miles_per_gallon)
		count += 1
		
		miles = float(input("Enter amount of miles driven or -1 to end: "))
		if miles == -1:
			break
	
if total > 0:	
		
	average = total / count
	print(f"The overall average miles/gallon was: {average}")
else: 
	print("No input collected")
	
	
		