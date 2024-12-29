import csv
from options.view_calendar import view_calendar

csv_data = []

def export_csv(data):
	with open("csv/export.csv", mode="w", newline="", encoding="utf8") as file:
		writer = csv.writer(file)
		writer.writerow(["Date and time", "Title", "Location"])
		for row in data:
			writer.writerow(row)

def export_calendar(connection):
	results = view_calendar(connection)
	for row in results:
		csv_data.append(row)
	export_csv(csv_data)