print(" " *9 + "Multiplication Table")
print(" "* 4, end="")
for header in range(1 , 10,):
	print(f"{header:>3}", end=" ")
print()
print(" "*4 + "-" * 35)

for multiply in range(1 , 10,):
	
	print(f"{multiply:>2} |", end="")

	for multiplication in range(1 , 10,):

		result = multiply * multiplication

		print(f"{result:>3}", end=" ")
	print()