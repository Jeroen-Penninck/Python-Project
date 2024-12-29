import sqlite3

def add_event(connection):
	date_and_time = input("Date and time: | YYYY-MM-DD hh:mm:ss | ")
	title = input("Title: ")
	location = input("Location: ")

	cursor = connection.cursor()

	cursor.execute("INSERT INTO events (date_and_time, title, location) VALUES (?, ?, ?)",
					(date_and_time, title, location))

	connection.commit()