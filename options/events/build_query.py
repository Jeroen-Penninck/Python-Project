from options.view_calendar import view_calendar

def build_query(connection):
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
		arg_count += 1
		if arg_count != 0:
			specified_query = specified_query + " AND" + q_title
		else:
			specified_query = base_query + "WHERE" + q_title
	if location != "":
		arg_count += 1
		if arg_count != 0:
			specified_query = specified_query + " AND" + q_location
		else:
			specified_query = base_query + "WHERE" + q_location
	if arg_count == 0:
		specified_query = base_query[:-1]

	return specified_query