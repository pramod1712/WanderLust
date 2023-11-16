"""
import sqlite3

con = sqlite3.connect('trip_planner1.db')
cur = con.cursor()

#add attribute to store user's country - to adjust prices, currencies
cur.execute("drop database if exists trip_planner_1")
con.commit()
print("done")
"""

"""
import mysql.connector

# Specify the connection parameters
config = {
    'user': 'root',
    'password': 'mysql',
    'host': 'localhost',
    'port': 3306,
    'database': 'art_gallery'
}

# Try to establish a connection
try:
    connection = mysql.connector.connect(**config)
    print("Connected to the database")
except mysql.connector.Error as err:
    print(f"Error: {err}")
"""

"""
joinres1 = cur.execute(
    "Select student.fname, student.lname, parents.fn, parents.mn from student inner join parents on student.id=parents.student_id")
print("Student join Parents")
for i in joinres1:
    print(i)

cur.execute("PRAGMA foreign_keys = 1")  # to enable foreign key constraint
query = '''insert into parents values(
'Ramaiah',
'Sita',
'Ganga2' ) 
'''
res2 = cur.execute("select * from parents")
data2 = res2.fetchall()
print("PARENTS TABLE")
print(data2)
data = cur.execute(query)
con.commit()

try:
    cur.execute(
        '''INSERT INTO academics (student_id, courses, branch, semester) VALUES  ('CS2', "B.Tech", "ECE", 4)''')
    con.commit()
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")
else:
    print("no error")

"""

"""
source = st.text_input("Enter your source:", "")
destination = st.text_input("Enter your destination:", "")
"""