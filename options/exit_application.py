def close_connections(connection):
	cursor = connection.cursor()

	cursor.close()
	connection.close()