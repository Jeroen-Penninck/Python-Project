#   Python-Project
### .gitignore
contains all the folders and files that should be ignored by my git repository
### main.py
start the application here: `python main.py`
### README.md
markdown file that you're reading right now
### requirement.txt
a file that contains all the requirements to run this application properly
>##  config
>### config.py
>stores the path to the database
>##  database
>### cal.db
>database for the calendar
>### database_manager.py
>initiliazes `cal.db` and create table events, connects to `cal.db` if it already exists
>##  exports
>default folders where exports are saved
>##  options
>### exit_application.py
>properly close cursor and connection before closing the appplication
>### export_calendar.py
>gives the user the choice to save the calendar into a csv or Excel file, then prompts the user to give it a name (the folder where this file will be saved may be changed by the user)\
**requires `pip install openpyxl`, however `pip install -r requirements.txt` should suffice**
>### view_calendar.py
>view the full calendar by displaying the content of events
>>## events
>>###    add_event.py
>>    asks the user to fill in the columns, then inserts them into the table events
>>###    build_query.py
>>    constructs the query with all notable possibilities, then returns the query in the form of a string
>>###    edit_event.py
>>    edit event using the build_query to select the correct events, asks the user for confirmation, then asks the user to write the SET clause
>>###    remove_event.py
>>    edit event using the build_query to select the correct events, then asks the user for confirmation