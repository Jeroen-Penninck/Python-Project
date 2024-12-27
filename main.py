from options.add_event import add_event
from options.view_calendar import view_calendar
from options.export_calendar import export_calendar

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
			if option == 2:
				valid = True
				view_calendar()
			if option == 3:
				valid = True
				export_calendar()

if __name__ == "__main__":
	Calendar().menu()