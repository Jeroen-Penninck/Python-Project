import sqlite3

def add_event():
	print(global_cursor)
	title = input("Title: ")
	date_and_time = input("Date and time: YYYY-MM-DD hh:mm:ss ")
	location = input("Location: ")



	cursor.commit()