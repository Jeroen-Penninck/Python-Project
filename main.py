from database.database_manager import database_manager

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
			match option:
				case 1:
					valid = True
					add_event()
				case 2:
					valid = True
					view_calendar()
				case 3:
					valid = True
					export_calendar()
				case 4:
					break

if __name__ == "__main__":
	database_manager()
	Calendar().menu()