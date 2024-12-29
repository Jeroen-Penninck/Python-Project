import csv
from options.view_calendar import view_calendar

def dialogue_file_extension():
	print("\nChoose file extension:\n1 Excel\n2 CSV\n")
	extension = input()
	if extension == "1":
		extension = ".xlsx"
	elif extension == "2":
		extension = ".csv"
	else:
		dialogue_file_extension()
	return extension

csv_data = []

def export_csv(data):
	file_extension = dialogue_file_extension()

	filename = input("Filename: ")
	filename = "exports/" + filename + file_extension
	with open(filename, mode="w", newline="", encoding="utf8") as file:
		writer = csv.writer(file)
		writer.writerow(["Date and time", "Title", "Location"])
		for row in data:
			writer.writerow(row)

def export_calendar(connection):
	results = view_calendar(connection)
	for row in results:
		csv_data.append(row)
	export_csv(csv_data)