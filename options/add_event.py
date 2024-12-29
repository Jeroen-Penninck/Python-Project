import sqlite3

def add_event(connection):
	title = input("Title: ")
	date_and_time = input("Date and time: YYYY-MM-DD hh:mm:ss ")
	location = input("Location: ")

	cursor = connection.cursor()

	cursor.execute("INSERT INTO events (title, date_and_time, location) VALUES (?, ?, ?)",
					(title, date_and_time, location))

	connection.commit()