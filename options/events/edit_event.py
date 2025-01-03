from options.events.build_query import build_query

def edit_results(results, query, connection):
	print("Edit the following event(s)?")
	print(results)
	print("\n1 Yes, edit")
	print("2 No, save\n")

	choice = int(input(""))
	if choice == 1:
		set_clause = input("SET ")
		edit_query = "UPDATE events SET " + set_clause + query
		connection.cursor().execute(edit_query)
		connection.commit()
		print("Edited database.")
	elif choice == 2:
		print("Database stays unchanged.")
	else:
		edit_results(results, query, connection)

def edit_event(connection):
	specified_query = build_query(connection)

	cursor = connection.cursor()
	cursor.execute(specified_query)
	results = cursor.fetchall()

	query_conditions = specified_query[21:]
	
	edit_results(results, query_conditions, connection)