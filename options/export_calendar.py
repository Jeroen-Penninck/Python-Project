import csv
import pandas as pd
from options.view_calendar import view_calendar

def back_to_main():
	print("\nBack to the main menu.")

def dialogue_file_extension():
	print("\nChoose file extension:\n1 Excel\n2 CSV\n\n9 Exit\n\n")
	res = input()
	if res == "1":
		res = ".xlsx"
	elif res == "2":
		res = ".csv"
	elif res == "9":
		res = "9"
	else:
		res = dialogue_file_extension()
	return res

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
	file_extension = dialogue_file_extension()

	if file_extension == "9":
		back_to_main()
	else:
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