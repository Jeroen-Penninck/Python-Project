def view_calendar(connection):
	cursor = connection.cursor()

	query =	"""
	SELECT *
	FROM events"""

	cursor.execute(query)

	results = cursor.fetchall()
	for row in results:
		print(row)