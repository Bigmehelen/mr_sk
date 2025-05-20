question_one_prompt = "What is your problem?: "
input(question_one_prompt);

response = input("Have you had this problem before(yes or no)?: ").lower();

match response:
	case "yes":
		print("Well, you have it again.")
	case "no":
		print("Well, you have it now")
	case _:
		print("Unknown command")