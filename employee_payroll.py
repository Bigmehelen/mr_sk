list = []

def add_employee_payroll(list , name, numOfHour, hourRate, fedTax, stateTax):
	list.append(f"Employee_name: {names}\n Hours_worked: {numOfHour}\n Pay_rate: {hourRate} \n Deductions:\n\tFederal_withholding: {fedTax} \n\tState_withholding: {stateTax}")
	
	if name[1] == names:
		print("name already exit")

def view_employee_payroll(list):
	for person in list:
		print(person)

def update_employee_payroll(list):
	for index, value in enumerate(list, name, numOfHour, hourRate, fedTax, stateTax):
		list[1] = update
		list[2] = update
		list[3] = update
		print(f"{index} , {value}")

def exit():
	Print("Thanks for coming")

while True:

	print("""
  Welcome to Semicolon Employee Payroll
	1. Add Employee Payroll
	2. View Employee Payroll
	3. Update Employee Payroll
	4. Exit

Enter your choice:
	""")
	net = 0
	user_input = input("Enter input (1-4): ")
	match (user_input):
		case "1": 
			names = input("Employee name: ")
			numOfHour = float(input("Hours Worked: "))
			hourRate= float(input("Pay Rate: "))
			fedTax = float(input("Enter federal witholding rate: "))
			stateTax = float(input("Enter state tax: "))
			gross_pay = numOfHour * hourRate
			print(f'Gross pay is: {gross_pay:.2f}') 
			federal = gross_pay * (fedTax / 100)
			state = gross_pay * (stateTax / 100)
			total = federal - state
			net = gross_pay - total
			print(f'Federal withholding (20.0%): {federal}')
			print(f'State withholding(9.0%): {state:.2f}')
			print = (f'Total deduction: {total}')
	print(add_employee_payroll(list, names, numOfHour, hourRate, fedTax, stateTax))
		
		case "2": 
			print(view_employee_payroll(list))
			
		case "3":
			names = input("Enter Employee name: ")
			numOfHour = float(input("Enter number of hours: "))
			hourRate = float(input("Hour pay Rate:"))
			fedTax = float(input("Enter federal witholding rate: "))
			stateTax = float(input("Enter state tax: "))




			
