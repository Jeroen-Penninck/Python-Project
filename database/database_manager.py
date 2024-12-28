import os, sqlite3
from config.config import DATABASE_PATH

def database_initializer():
	if os.path.isfile(DATABASE_PATH) == False:
		connection = sqlite3.connect(DATABASE_PATH)
		print("create db")
	else:
		print("db already exists")