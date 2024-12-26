import os
from options.add_event import add_event

print("\n *************************************\n | Super Simple Commandline Calendar |\n *************************************\n")

class Calendar:
	def __init__(self):
		pass

	def menu(self):
		valid = False
		while valid == False:
			print("1 Add Event")
			print("2 View Calendar")
			print("3 Export Calendar")
			print("4 Exit Application")

			option = int(input("\n"))
			
			if option == 1:
				valid = True
				add_event()

if __name__ == "__main__":
	Calendar().menu()