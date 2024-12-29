from options.view_calendar import view_calendar

def remove_results(results, query, connection):
	print("Remove the following event(s)?")
	print(results)
	print("\n1 Yes, remove")
	print("2 No, save\n")

	choice = int(input(""))
	if choice == 1:
		delete_query = "DELETE FROM events " + query
		connection.cursor().execute(delete_query)
		connection.commit()
		print("Deleted from database.")
	elif choice == 2:
		print("Database stays unchanged.")
	else:
		remove_results(results, query)

def remove_event(connection):
	view_calendar(connection)

	print("\nSet parameters: (leave non-specified empty)")
	date_and_time = input("Date and time: ")
	q_date_and_time = f"WHERE date_and_time LIKE '{date_and_time}'"
	title = input("Title: ")
	q_title = f" title LIKE '{title}'"
	location = input("Location: ")
	q_location = f" location LIKE '{location}'"

	base_query = "SELECT * FROM events "

	arg_count = 0

	if date_and_time != "":
		specified_query = base_query + q_date_and_time
		arg_count += 1
	if title != "":
		if arg_count != 0:
			specified_query = specified_query + " AND" + q_title
		else:
			specified_query = base_query + "WHERE" + q_title
	if location != "":
		if arg_count != 0:
			specified_query = specified_query + " AND" + q_location
		else:
			specified_query = base_query + "WHERE" + q_location

	cursor = connection.cursor()
	print()
	cursor.execute(specified_query)

	query_conditions = specified_query[21:]

	results = cursor.fetchall()

	remove_results(results, query_conditions, connection)