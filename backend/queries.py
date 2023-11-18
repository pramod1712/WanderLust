import sys
import os
import sqlite3

# Add the path to the outer directory containing utils.py to sys.path
outer_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(outer_dir)

# Now import the module from the outer directory
from utils import get_country_code

con = sqlite3.connect('trip_plannerr1.db')
cur = con.cursor()

#cur.execute("select concat(Name, City, Country) as search_input1 from Destinations")


def get_next_tripid(country_name):
    country_code = get_country_code(country_name)
    # SQLite query to find the last inserted record for a specific country ID
    query = f"SELECT * FROM Trip WHERE TripID LIKE '{country_code}%' ORDER BY ROWID DESC LIMIT 1"

    # Execute the query using the cursor
    cur.execute(query)

    # Fetch the result
    last_inserted_record = cur.fetchone()

    # Display the result
    if last_inserted_record:
        print("Last inserted record for", country_code, ":", last_inserted_record)
        return last_inserted_record
    else:
        return -1
    
get_next_tripid('India')