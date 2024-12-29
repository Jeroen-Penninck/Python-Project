import sqlite3

def add_event(cursor):
	title = input("Title: ")
	date_and_time = input("Date and time: YYYY-MM-DD hh:mm:ss ")
	location = input("Location: ")

	cursor.execute("INSERT INTO events (title, date_and_time, location) VALUES (?, ?, ?)",
					(title, date_and_time, location))

	#cursor.commit()