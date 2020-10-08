import sqlite3

# Connect to Database
connection = sqlite3.connect('department.db')

# Create a Cursor
c = connection.cursor()


# Create a Table
c.execute("""CREATE TABLE department (
    dept_name text,
    dept_num integer,
    ph_num integer,
    est_date text
)
""")

# input data in a database table
