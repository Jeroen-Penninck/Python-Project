import os, sqlite3
from config.config import DATABASE_PATH

def database_initializer():
	if os.path.isfile(DATABASE_PATH) == False:
		connection = sqlite3.connect(DATABASE_PATH)
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE events (title nvarchar(255) NOT NULL, date_and_time datetime NOT NULL, location nvarchar(255))")
	else:
		connection = sqlite3.connect(DATABASE_PATH)

	return connection