number = int(input("Enter a number: "));
print(number)

original = number;
reversed = 0;
while number > 0:
	digit = number % 10
	reversed = reversed * 10 + digit
	number = number // 10
if original == reversed : 
	print("This number is a palindrome number")
else: 
	print("This is not a palindrome number")