import csv
from options.view_calendar import view_calendar

def dialogue_file_extension():
	print("\nChoose file extension:\n1 Excel\n2 CSV\n")
	extension = input()
	if extension == "1":
		extension = ".xlsb"
	elif extension == "2":
		extension = ".csv"
	else:
		dialogue_file_extension()
	return extension

csv_data = []

def export_csv(data):
	file_extension = dialogue_file_extension()

	filename = input("Filename: ")
	if filename[-4:] == ".csv" or filename[-5:] == ".xlsx":
		filename = "exports/" + filename
	else:
		filename = "exports/" + filename + file_extension

	with open(filename, mode="w", newline="", encoding="utf8") as file:
		writer = csv.writer(file)
		writer.writerow(["Date and time", "Title", "Location"])
		for row in data:
			writer.writerow(row)

def export_calendar(connection):
	results = view_calendar(connection)
	export_csv(results)