from database.database_manager import database_initializer

from options.add_event import add_event
from options.view_calendar import view_calendar
from options.export_calendar import export_calendar
from options.exit_application import close_connections

print("\n *************************************\n | Super Simple Commandline Calendar |\n *************************************\n")

class Calendar:
	def __init__(self):
		self.connection = database_initializer()

	def menu(self):
		valid = False
		while valid == False:
			print("\n1 Add Event")
			print("2 View Calendar")
			print("3 Export Calendar")
			print("4 Exit Application")

			option = int(input("\n"))
			print()
			match option:
				case 1:
					add_event(self.connection)
				case 2:
					view_calendar(self.connection)
				case 3:
					export_calendar()
				case 4:
					close_connections(self.connection)
					valid = True

if __name__ == "__main__":
	Calendar().menu()