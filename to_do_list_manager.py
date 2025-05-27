def in_main(number):
	running = True 
	while running:
		print("""

		===To do list manager===
		1. Add a task
		2. View tasks
		3. mark task as complete
		4. Delete a task
		5. Exit

		Enter your choice: 
		""")
		in_main("Choose an option: ")
		match in_main_menu:
			case 5:
				running = False
			case _: 
				print("Invalid Input")
				continue

def add_a_task(number):

	in_to_do_list = input("Choose an option: ")
	match in_to_do_list:
		case 1:
			print("""
		1. Add a task
		press 0 to go back
			""")
			user_add = input("Choose an option: ")
			match user_add:
				case 1:
					print("""
				1. Buy Groceries [x] finish(homework)
				press 0 to go back
					""")
					user_add_task = True
					while user_add_task:
						view = input("Choose an option: ")
						match view:
							case 0: 
								user_add_task = False
							case _:
								print("Invalid input")
								continue

			
			in_add = True
			while in_add:
				add = input("Choose an option: ")
				match add:
					case 0: 
						in_add = False
					case _:
						print("Invalid input")
						continue

def view_tasks(number):
	in_to_do_list = input("Choose an option: ")
	match in_to_do_list:
		case 2:
			print("""
		2. Add a task
		press 0 to go back
			""")
			in_view = True
			while in_view:
				view = input("Choose an option: ")
				match view:
					case 0: 
						in_view = False
					case _:
						print("Invalid input")
						continue









			

			

	


		



