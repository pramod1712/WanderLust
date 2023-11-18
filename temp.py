#not working
"""
                        description, budget = trip_info
                        st.info(f"Description: {description}")
                        st.info(f"Budget: {budget}")
"""

"""
                        if trip_info:
                            description, budget = trip_info
                            st.info(f"Description: {description}")
                            st.info(f"Budget: {budget}")
                        else:
                            st.info("No details found for the selected destination.")
""" 
"""
st.image("https://wallpapers.com/images/hd/vibrant-mount-fuji-lake-5e9i6zkcn925n5zb.jpg")

                clicked = clickable_images(
                [
                    "https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=700",
                    "https://images.unsplash.com/photo-1565372195458-9de0b320ef04?w=700",
                    "https://images.unsplash.com/photo-1582550945154-66ea8fff25e1?w=700",
                    "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",
                    "https://images.unsplash.com/photo-1518727818782-ed5341dbd476?w=700",
                ],
                titles=[f"Image #{str(i)}" for i in range(5)],
                div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
                img_style={"margin": "5px", "height": "200px"},
)

                st.markdown(f"Image #{clicked} clicked" if clicked > -1 else "No image clicked")"""


#old codes

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