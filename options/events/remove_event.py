from options.events.build_query import build_query

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
		remove_results(results, query, connection)

def remove_event(connection):
	specified_query = build_query(connection)
	cursor = connection.cursor()	
	cursor.execute(specified_query)

	query_conditions = specified_query[21:]

	results = cursor.fetchall()

	remove_results(results, query_conditions, connection)