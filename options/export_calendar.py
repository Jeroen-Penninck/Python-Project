import csv
import pandas as pd
from options.view_calendar import view_calendar

def back_to_main():
	print("\nBack to the main menu.")

def dialogue_file_extension():
	print("\nChoose file extension:\n1 Excel\n2 CSV\n\n4 Exit\n\n")
	extension = input()
	if extension == "1":
		extension = ".xlsx"
	elif extension == "2":
		extension = ".csv"
	elif extension == "4":
		extension = 4
	else:
		extension = dialogue_file_extension()
	return extension

def export_csv(filename, data):
	with open(filename, mode="w", newline="", encoding="utf8") as file:
		writer = csv.writer(file)
		writer.writerow(["Date and time", "Title", "Location"])
		for row in data:
			writer.writerow(row)

def export_xlsx(filename, data):
	df = pd.DataFrame(data, columns=["Date and time", "Title", "Location"])
	df.to_excel(filename, index=False)

def export_handler(data):
	if dialogue_file_extension() == 4:
		back_to_main()
	else:
		file_extension = dialogue_file_extension()
	
		filename = input("Filename: ")
	
		if filename[-4:] == ".csv":
			filename = "exports/" + filename
			export_csv(filename, data)
		elif filename[-5:] == ".xlsx":
			filename = "exports/" + filename
			export_xlsx(filename, data)
		else:
			filename = "exports/" + filename + file_extension
			if file_extension == ".csv":
				export_csv(filename, data)
			else:
				export_xlsx(filename, data)

def export_calendar(connection):
	results = view_calendar(connection)
	export_handler(results)