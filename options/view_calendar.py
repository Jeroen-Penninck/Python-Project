def view_calendar(connection):
	cursor = connection.cursor()

	view_query = """
	SELECT *
	FROM events
	ORDER BY date_and_time, title, location"""

	cursor.execute(view_query)

	results = cursor.fetchall()
	for row in results:
		print(row)

	return results