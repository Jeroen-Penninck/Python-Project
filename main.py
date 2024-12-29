from database.database_manager import database_initializer

from options.events.add_event import add_event


from options.view_calendar import view_calendar
from options.export_calendar import export_calendar
from options.exit_application import close_connections

print("\n *************************************\n | Super Simple Commandline Calendar |\n *************************************")

class Calendar:
	def __init__(self):
		self.connection = database_initializer()

	def menu(self):
		valid = False
		while valid == False:
			print("\n1 Add Event")
			print("2 Edit Event")
			print("3 Remove Event")
			print("4 View Calendar")
			print("5 Export Calendar")
			print("\n9 Exit Application")

			option = int(input("\n\n"))
			print()
			match option:
				case 1:
					add_event(self.connection)
				#case 2:

				#case 3:

				case 4:
					view_calendar(self.connection)
				case 5:
					export_calendar(self.connection)
				case 9:
					close_connections(self.connection)
					valid = True

if __name__ == "__main__":
	Calendar().menu()