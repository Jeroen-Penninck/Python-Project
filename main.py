

print("\n *************************************\n | Super Simple Commandline Calendar |\n *************************************\n")

class Menu:
	valid = False
	valid_options = [1,2,3,4]
	while valid == False:
		print("1 Add Event")
		print("2 View Calendar")
		print("3 Export Calendar")
		print("4 Exit Application")

		option = int(input())
		for v in valid_options:
			if v == option:
				valid = True