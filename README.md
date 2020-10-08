# Project_SQL

Simple Web interface that executes the queries and show the query results

#department.py

# Create a Table

c.execute("""CREATE TABLE department (
dept_name text,
dept_num integer,
ph_num integer,
est_date text
)
""")

# input data in a database table

file_data = [i.strip('\n').split(', ') for i in open('DEPARTMENT.txt')]

c.executemany('INSERT INTO department VALUES (?, ?, ?,?)', file_data)

#

#
