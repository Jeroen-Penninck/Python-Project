import sqlite3

def add_event(connection):
	date_and_time = ""
	while date_and_time == "":
		date_and_time = input("[required] Date and time: | YYYY-MM-DD hh:mm:ss | ")
	title = ""
	while title == "":
		title = input("[required] Title: ")
	location = input("Location: ")

	cursor = connection.cursor()

	cursor.execute("INSERT INTO events (date_and_time, title, location) VALUES (?, ?, ?)",
					(date_and_time, title, location))

	connection.commit()