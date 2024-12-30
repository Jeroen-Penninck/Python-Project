from options.events.build_query import build_query

def edit_event(connection):
	specified_query = build_query(connection)
	print(specified_query)