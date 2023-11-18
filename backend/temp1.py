import sqlite3
import streamlit as st
con = sqlite3.connect('trip_plannerr1.db')
cur = con.cursor()


# Establish SQLite connection and create a cursor
conn = sqlite3.connect('your_database_name.db')
cursor = conn.cursor()

# Check if the Trip table exists, create it if it doesn't
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Trip (
        TripID TEXT PRIMARY KEY,
        TripName TEXT NOT NULL,
        RecommendedStartMonth TEXT,
        RecommendedEndMonth TEXT,
        Description TEXT,
        Budget NUMERIC(10,2),
        ImageURL TEXT
    )
''')
conn.commit()

# Your Streamlit code
formbtn = st.button("Add a New Trip")

if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False

if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True
    
    st.subheader("Trip Information Form")
    
    with st.form(key='trip_info'):
        st.write('New Trip')
        
        trip_id = st.text_input(label="Trip ID")
        trip_name = st.text_input(label="Trip Name")
        start_month = st.text_input(label="Recommended Start Month")
        end_month = st.text_input(label="Recommended End Month")
        description = st.text_area(label="Description")
        budget = st.number_input(label="Budget", value=0.0)
        #image_url = st.text_input(label="Image URL")
        
        submit_form = st.form_submit_button(label="Register Trip")
        
        if submit_form:
            if trip_id and trip_name and start_month and end_month and description and budget:
                # Insert user information into the Trip table
                try:
                    cursor.execute(
                        "INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES (?, ?, ?, ?, ?, ?)",
                        (trip_id, trip_name, start_month, end_month, description, budget)
                    )
                    conn.commit()
                    st.success(f"Trip registered successfully!")
                except sqlite3.IntegrityError:
                    st.warning("TripID already exists, please use a different ID.")
            else:
                st.warning("Please fill all the fields in the form.")

# Close the SQLite connection
conn.close()
