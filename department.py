import sqlite3

# Connect to Database
connection = sqlite3.connect('department.db')

# Create a Cursor
c = connection.cursor()


# fetch the data
c.execute("SELECT * FROM department")
print(c.fetchall())


# Commit the command
connection.commit()

# Close the Connection
connection.close()
