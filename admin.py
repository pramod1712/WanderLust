import streamlit as st
import streamlit_authenticator as stauth
from dependancies_admin import sign_up, fetch_admins
import sqlite3
import pandas as pd

def fetch_trip_data(trip_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute("SELECT * FROM trip WHERE TripID = ?", (trip_id,))
    trip_data = cur.fetchone()
    return trip_data


def fetch_dest_data(dest_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute("SELECT * FROM Destination WHERE DestinationID = ?", (dest_id,))
    dest_data = cur.fetchone()
    return dest_data


def fetch_accmd_data(accmd_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute(
        "SELECT * FROM Accomodation WHERE AccomodationID = ?", (accmd_id,))
    accmd_data = cur.fetchone()
    return accmd_data


def fetch_transport_data(trans_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute(
        "SELECT * FROM Transportation WHERE TransportID = ?", (trans_id,))
    trans_data = cur.fetchone()
    return trans_data


def fetch_recommendation_data(rcmd_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute(
        "SELECT * FROM Recommendation WHERE RecommendationID = ?", (rcmd_id,))
    rcmd_data = cur.fetchone()
    return rcmd_data


def fetch_activity_data(act_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute(
        "SELECT * FROM Activity WHERE ActivityID = ?", (act_id,))
    act_data = cur.fetchone()
    return act_data


def fetch_weather_data(w_id):
    # Fetch existing values for the specified trip_id from the 'trip' table
    cur.execute(
        "SELECT * FROM Weather WHERE WeatherID = ?", (w_id,))
    wthr_data = cur.fetchone()
    return wthr_data


try:
    con = sqlite3.connect('trip_planner2.db')
    cur = con.cursor()
    print("connected")
    # con = st.connection('trip_planner2', type='sql')
except:
    st.error("could not connect to database")

st.set_page_config(page_title='Trip Planner -PES',
                   page_icon='🦸‍♂️', initial_sidebar_state='collapsed'
                   )
st.title("Trip Planner -PES Admin Panel")

try:
    admins = fetch_admins()
    emails = []
    usernames = []
    passwords = []

    for user in admins:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {
            'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(
        credentials, cookie_name='TripPlannerAdmin', key='abcdef', cookie_expiry_days=1)

    email, authentication_status, username = Authenticator.login(
        ':orange[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome Admin {username}')
                Authenticator.logout('Log Out', 'sidebar')


                def render_home():
                    st.title("Home Page")
                    st.write("Welcome to the Home Page!")
                    st.write("Click on the sidebar to navigate to other pages.")
                    st.markdown("---")
                    cur.execute("SELECT COUNT(*) FROM trip")
                    count = cur.fetchone()[0]
                    st.success(f"Total number of trips we are offering are {count}")

                    cur.execute("SELECT COUNT(*) FROM Destination")
                    count = cur.fetchone()[0]
                    st.error(
                        f"Total number of Destinations we are in {count}")
                    
                    cur.execute("SELECT COUNT(*) FROM Accomodation")
                    count = cur.fetchone()[0]
                    st.success(
                        f"Total number of Accomodation privileges we are having {count}")
                    
                    cur.execute("SELECT COUNT(*) FROM Transportation")
                    count = cur.fetchone()[0]
                    st.error(
                        f"Total number of transport ways we are having {count}")
                    
                    cur.execute("SELECT COUNT(*) FROM Recommendation")
                    count = cur.fetchone()[0]
                    st.success(
                        f"Total number of Recommendation packages we are having {count}")

                    cur.execute("SELECT COUNT(*) FROM Activity")
                    count = cur.fetchone()[0]
                    st.error(
                        f"Total number of Activities we are having {count}")
                    
                    cur.execute("SELECT COUNT(*) FROM Transportation")
                    count = cur.fetchone()[0]
                    st.success(
                        f"Total information about weather in {count} different places")

                    

                def render_create():
                    st.title("Insert or create into DB from this page")
                    st.write("Click on the sidebar to navigate to other pages.")
                    
                    # Your Streamlit code
                    formbtn1 = st.button("Add a New Trip")

                    if "formbtn1_state" not in st.session_state:
                        st.session_state.formbtn1_state = False

                    if formbtn1 or st.session_state.formbtn1_state:
                        st.session_state.formbtn1_state = True

                        st.subheader("Trip Information Form")

                        with st.form(key='trip_info'):
                            st.write('New Trip')

                            trip_id = st.text_input(label="Trip ID")
                            trip_name = st.text_input(label="Trip Name")
                            start_month = st.text_input(
                                label="Recommended Start Month")
                            end_month = st.text_input(
                                label="Recommended End Month")
                            description = st.text_area(label="Description")
                            budget = st.number_input(label="Budget", value=0.0)
                            # image_url = st.text_input(label="Image URL")

                            submit_form = st.form_submit_button(
                                label="Register Trip")

                            if submit_form:
                                if trip_id and trip_name and start_month and end_month and description and budget:
                                    # Insert user information into the Trip table
                                    try:
                                        cur.execute(
                                            "INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES (?, ?, ?, ?, ?, ?)",
                                            (trip_id, trip_name, start_month,
                                            end_month, description, budget)
                                        )
                                        con.commit()
                                        st.success(
                                            f"Trip registered successfully!")
                                    except sqlite3.IntegrityError:
                                        st.warning(
                                            "TripID already exists, please use a different ID.")
                                else:
                                    st.warning(
                                        "Please fill all the fields in the form.")
                    st.markdown("---")
                    formbtn2 = st.button("Add a new dest")

                    if "formbtn2_state" not in st.session_state:
                        st.session_state.formbtn2_state = False

                    if formbtn2 or st.session_state.formbtn2_state:
                        st.session_state.formbtn2_state = True

                        st.subheader("Add a New Destination")
                        with st.form(key='add_destination_form'):
                            # Collect destination details from the user
                            trip_id = st.text_input("Trip ID")
                            # Limit the length if needed
                            destination_id = st.text_input("Destination ID")
                            # Adjust the maximum length accordingly
                            name = st.text_input("Name")
                            country = st.text_input("Country")
                            city = st.text_input("City")
                            description = st.text_area("Description")

                            # Check if all fields are filled
                            if st.form_submit_button("Submit") and all([trip_id, destination_id, name, country, city]):
                                # Insert the new destination into the database
                                cur.execute(
                                    "INSERT INTO Destination (TripID, DestinationID, Name, Country, City, Description) VALUES (?, ?, ?, ?, ?, ?);",
                                    (trip_id, destination_id, name,
                                    country, city, description)
                                )
                                con.commit()

                                st.success(
                                    f"Destination added successfully!")
                    st.markdown("---")
                    formbtn3 = st.button("Transportation")

                    if "formbtn3_state" not in st.session_state:
                        st.session_state.formbtn3_state = False

                    if formbtn3 or st.session_state.formbtn3_state:
                        st.session_state.formbtn3_state = True

                        st.subheader("Add New Transportation")

                        # Create a form
                        with st.form(key='add_transportation_form'):
                            # Collect transportation details from the user
                            transport_id = st.text_input("Transport ID")
                            mode = st.text_input("Mode")
                            departure_datetime = st.text_input("Departure Datetime")
                            arrival_datetime = st.text_input("Arrival Datetime")
                            departure_location = st.text_input("Departure Location")
                            arrival_location = st.text_input("Arrival Location")
                            cost = st.number_input("Cost")
                            submit_form = st.form_submit_button(
                                                    label="Register")

                            if submit_form:

                            # Check if all fields are filled
                                if all([transport_id, mode, departure_datetime, arrival_datetime, departure_location, arrival_location, cost]):
                                    # Insert the new transportation into the database
                                    cur.execute(
                                        "INSERT INTO Transportation (TransportID, Mode, DepartureDatetime, ArrivalDatetime, DepartureLocation, ArrivalLocation, Cost) VALUES (?, ?, ?, ?, ?, ?, ?);",
                                        (transport_id, mode, departure_datetime, arrival_datetime,
                                        departure_location, arrival_location, cost)
                                    )
                                    con.commit()
                                    st.success("Transportation added successfully!")
                    st.markdown("---")
                    formbtn4 = st.button("Add a new Accomodation")

                    if "formbtn4_state" not in st.session_state:
                        st.session_state.formbtn4_state = False

                    if formbtn4 or st.session_state.formbtn4_state:
                        st.session_state.formbtn4_state = True


                        st.subheader("Add New Accomodation")

                    # Create a form
                        with st.form(key='add_Accomodation_form'):
                            # Collect accommodation details from the user
                            trip_id = st.text_input("Trip ID")
                            accomodation_id = st.text_input("Accomodation ID")
                            name = st.text_input("Name")
                            accomodation_type = st.text_input("Type")
                            location = st.text_input("Location")
                            cost = st.number_input("Cost")

                            submit_form = st.form_submit_button(
                                    label="Register")

                            
                            if submit_form and trip_id and accomodation_id and name and accomodation_type and location and cost:
                                    # Insert the new accommodation into the database
                                cur.execute(
                                    "INSERT INTO Accomodation (TripID, AccomodationID, Name, Type, Location, Cost) VALUES (?, ?, ?, ?, ?, ?);",
                                    (trip_id, accomodation_id, name,
                                    accomodation_type, location, cost)
                                )
                                con.commit()
                                st.success("Accomodation added successfully!")
                    st.markdown("---")
                    formbtn5 = st.button("Recommendation")

                    if "formbtn5_state" not in st.session_state:
                        st.session_state.formbtn5_state = False

                    if formbtn5 or st.session_state.formbtn5_state:
                        st.session_state.formbtn5_state = True

                        st.subheader("Add New Recommendation")

                            # Create a form
                        with st.form(key='add_recommendation_form'):
                            # Collect recommendation details from the user
                            recommendation_id = st.text_input(
                                "Recommendation ID")
                            recommendation_type = st.text_input("Type")
                            name = st.text_input("Name")
                            description = st.text_area("Description")
                            rating = st.number_input("Rating")
                            submit_form = st.form_submit_button("Submit")

                                # Check if all fields are filled
                            if submit_form and all([recommendation_id, recommendation_type, name,description,rating]):
                                # Insert the new recommendation into the database
                                cur.execute("INSERT INTO Recommendation (RecommendationID, Type, Name, Description, Rating) VALUES (?, ?, ?, ?, ?);", (
                                    recommendation_id, recommendation_type, name, description, rating))
                                con.commit()
                                st.success(
                                    "Recommendation added successfully!")
                    st.markdown("---")
                    formbtn6 = st.button("Activity")

                    if "formbtn6_state" not in st.session_state:
                        st.session_state.formbtn6_state = False

                    if formbtn6 or st.session_state.formbtn6_state:
                        st.session_state.formbtn6_state = True

                        st.subheader("Add New Activity")

                        # Create a form
                        with st.form(key='add_activity_form'):
                            # Collect activity details from the user
                            activity_id = st.text_input("Activity ID")
                            name = st.text_input("Name")
                            description = st.text_area("Description")
                            date = st.date_input("Date")
                            time = st.time_input("Time")
                            cost = st.number_input("Cost")
                            submit_form = st.form_submit_button("Submit")
                            # Check if all fields are filled
                            if submit_form and activity_id and name and description and date and time and cost:
                                # Insert the new activity into the database
                                    
                                    insert_query = """
    INSERT INTO Activity (ActivityID, Name, Description, Date, Time, Cost)
    VALUES (?, ?, ?, ?, ?, ?)
"""

# Replace the following values with the actual data you want to insert
                                    data_to_insert = (activity_id, name, description,date, str(time), cost)

# Execute the query
                                    cur.execute(insert_query, data_to_insert)
                                    
                                    
                                    con.commit()
                                    st.success("Activity added successfully!")
                        
                    st.markdown("---")
                    formbtn7 = st.button("Weather")

                    if "formbtn7_state" not in st.session_state:
                        st.session_state.formbtn7_state = False

                    if formbtn7 or st.session_state.formbtn7_state:
                        st.session_state.formbtn7_state = True

                        st.subheader("Add New weather")
                        # Create a form
                        with st.form(key='add_weather_form'):
                            # Collect weather details from the user
                            weather_id = st.text_input("Weather ID")
                            date = st.date_input("Date")
                            temp = st.number_input("Temperature", value=0.0, step=0.1)
                            conditions = st.text_input("Conditions")
                            b=st.form_submit_button("Submit")
                        # Check if all fields are filled
                            if b and all([weather_id, date, temp, conditions]):
                            # Insert the new weather details into the database
                                cur.execute(
                                    "INSERT INTO Weather (WeatherID, Date, Temp, Conditions) VALUES (?, ?, ?, ?);",
                                    (weather_id, date, temp, conditions)
                                )
                                con.commit()
                                st.success(
                                    "Weather details added successfully!")

                

                
                    

                def render_read():
                    st.title("To view values")
                    st.write("Click on the sidebar to navigate to other pages.")
                    

                    if (st.button("display trips")):
                        st.write("view info about the trips")
                        trip_data = cur.execute('SELECT * FROM trip').fetchall()
                        column_names = [description[0] for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)
                        
                    st.markdown("---")

                    if (st.button("display destinations")):
                        st.write("view info about the destinations")
                        trip_data = cur.execute('SELECT * FROM Destination').fetchall()
                        column_names = [description[0] for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)

                    st.markdown("---")
                    if (st.button("display Accomodations")):
                        st.write("view info about the Accomodations")
                        trip_data = cur.execute(
                            'SELECT * FROM Accomodation').fetchall()
                        column_names = [description[0]
                                        for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)

                    st.markdown("---")
                    if (st.button("display Transportation")):
                        st.write("view info about the Transportation")
                        trip_data = cur.execute(
                            'SELECT * FROM Transportation').fetchall()
                        column_names = [description[0]
                                        for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)
                    st.markdown("---")

                    if (st.button("display Recommendation")):
                        st.write("view info about the Recommendation")
                        trip_data = cur.execute(
                            'SELECT * FROM Recommendation').fetchall()
                        column_names = [description[0]
                                        for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)
                    st.markdown("---")
                    if (st.button("display Activity")):
                        st.write("view info about the Activity")
                        trip_data = cur.execute(
                            'SELECT * FROM Activity').fetchall()
                        column_names = [description[0]
                                        for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)
                    st.markdown("---")
                    if (st.button("display Weather")):
                        st.write("view info about the Weather")
                        
                        trip_data = cur.execute(
                            'SELECT * FROM Weather').fetchall()
                        column_names = [description[0]
                                        for description in cur.description]
                        df_trip = pd.DataFrame(trip_data, columns=column_names)
                        st.dataframe(df_trip)

                    

                def render_update():
                    st.title("To update values in DB")
                    st.write("Click on the sidebar to navigate to other pages.")

                    formbtn11 = st.button("update a Trip")
                    
                    if "formbtn11_state" not in st.session_state:
                        st.session_state.formbtn11_state = False

                    if formbtn11 or st.session_state.formbtn11_state:
                        st.session_state.formbtn11_state = True
                    
                        cur.execute("SELECT TripID FROM trip")
                        trip_ids = [row[0] for row in cur.fetchall()]
                        trip_id_to_edit = st.selectbox(
                            "Select a TripID", trip_ids)
                        

                    
                            # Fetch existing data for the specified trip_id
                        existing_data = fetch_trip_data(trip_id_to_edit)
                        
                        if existing_data:
                                # Display the existing dat
                                with st.form(key='trip_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                    st.subheader("Edit Trip Details:")
                                    new_trip_name = st.text_input("New Trip Name", value=existing_data[1])
                                    new_start_month = st.text_input("New Start Month", value=existing_data[2])
                                    new_end_month = st.text_input("New End Month", value=existing_data[3])
                                    new_description = st.text_area("New Description", value=existing_data[4])
                                    new_budget = st.number_input("New Budget", value=existing_data[5])
                                    
                                    if(st.form_submit_button(label="UPDATE Trip") and new_budget and new_description and new_end_month and new_start_month and new_trip_name):
                                        cur.execute("UPDATE trip SET TripName=?, RecommendedStartMonth=?, RecommendedEndMonth=?, Description=?, Budget=? WHERE TripID=?",
                                                    (new_trip_name, new_start_month, new_end_month, new_description, new_budget, trip_id_to_edit))
                                        con.commit()
                                        st.success("Successfully updated!!")
                    st.markdown("---")
                    formbtn12 = st.button("update Destination")

                    if "formbtn12_state" not in st.session_state:
                        st.session_state.formbtn12_state = False

                    if formbtn12 or st.session_state.formbtn12_state:
                        st.session_state.formbtn12_state = True

                        cur.execute("SELECT DestinationID FROM Destination")
                        dest_ids = [row[0] for row in cur.fetchall()]
                        dest_id_to_edit = st.selectbox(
                            "Select a DestinationID", dest_ids)
                        
                        # Get the trip_id input from the admin

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_dest_data(dest_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='dest_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Destination Details:")
                                new_destname = st.text_input(
                                    "New Destination Name", value=existing_data[2])
                                new_country = st.text_input(
                                    "country", value=existing_data[3])
                                new_city = st.text_input(
                                    "New city", value=existing_data[4])
                                new_description = st.text_area(
                                    "New Description", value=existing_data[5])
                                
                                if (st.form_submit_button(label="UPDATE Dest") and new_destname and new_description and new_city and new_country ):
                                    cur.execute("UPDATE Destination SET Name=?, Country=?, City=?, Description=? WHERE DestinationID=?",
                                                (new_destname, new_country, new_city, new_description, dest_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")
                    st.markdown("---")
                    formbtn13 = st.button("update Accommodation")

                    if "formbtn13_state" not in st.session_state:
                        st.session_state.formbtn13_state = False

                    if formbtn13 or st.session_state.formbtn13_state:
                        st.session_state.formbtn13_state = True

                        cur.execute("SELECT AccomodationID FROM Accomodation")
                        acmd_ids = [row[0] for row in cur.fetchall()]
                        accmd_id_to_edit = st.selectbox(
                            "Select a AccommodationID", acmd_ids)
                        
                        # Get the trip_id input from the admin

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_accmd_data(accmd_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='dest_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Accommodation Details:")
                                new_accmdname = st.text_input(
                                    "Accomodation Name", value=existing_data[2])
                                new_type = st.text_input(
                                    "type", value=existing_data[3])
                                new_location = st.text_input(
                                    "Location", value=existing_data[4])
                                new_cost = st.text_input(
                                    "cost", value=existing_data[5])

                                if (st.form_submit_button(label="UPDATE Accmd") and new_accmdname and new_type and new_location and new_cost):
                                    cur.execute("UPDATE Accomodation SET Name=?, Type=? ,Location=?, Cost=? WHERE AccomodationID=?",
                                                (new_accmdname, new_type, new_location, new_cost, accmd_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")

                    st.markdown("---")

                    formbtn14 = st.button("update Transportation")

                    if "formbtn14_state" not in st.session_state:
                        st.session_state.formbtn14_state = False

                    if formbtn14 or st.session_state.formbtn14_state:
                        st.session_state.formbtn14_state = True

                        cur.execute("SELECT TransportID FROM Transportation")
                        transp_ids = [row[0] for row in cur.fetchall()]
                        transport_id_to_edit = st.selectbox(
                            "Select a TransportID", transp_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_transport_data(transport_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Transport_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Transport Details:")
                                new_mode = st.text_input("mode", value=existing_data[1])
                                new_ddt = st.text_input("Departure Date time", value=existing_data[2])
                                new_adt = st.text_input("Arrival Date time", value=existing_data[3])
                                new_dl = st.text_input("Departure Location", value=existing_data[4])
                                new_al = st.text_input("Arrival Location", value=existing_data[5])
                                new_cost = st.text_input("Cost",value=existing_data[6])
                                if (st.form_submit_button(label="UPDATE Transport") and new_mode and new_ddt and new_adt and new_dl and new_al and new_cost):
                                    cur.execute("UPDATE Transportation SET Mode=?, DepartureDatetime=? ,ArrivalDatetime=?, DepartureLocation=?, ArrivalLocation=?, Cost=? WHERE TransportID=?",
                                                (new_mode, new_ddt, new_adt, new_dl,new_al,new_cost, transport_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")
                    
                    st.markdown("---")
                    formbtn15 = st.button("update Recommendation")

                    if "formbtn15_state" not in st.session_state:
                        st.session_state.formbtn15_state = False

                    if formbtn15 or st.session_state.formbtn15_state:
                        st.session_state.formbtn15_state = True

                        cur.execute(
                            "SELECT RecommendationID FROM Recommendation")
                        rcmd_ids = [row[0] for row in cur.fetchall()]
                        rcmd_id_to_edit = st.selectbox(
                            "Select a RecommendationID", rcmd_ids)
                        # Get the trip_id input from the admin

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_recommendation_data(
                            rcmd_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Recommendation_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Recommendation Details:")
                                new_type = st.text_input(
                                    "Type", value=existing_data[1])
                                new_name = st.text_input(
                                    "Name", value=existing_data[2])
                                new_desc = st.text_area(
                                    "Description", value=existing_data[3])
                                new_rtng = st.text_input(
                                    "Rating", value=existing_data[4])
                                
                                if (st.form_submit_button(label="UPDATE Recommendation") and new_type and new_name and new_desc and new_rtng ):
                                    cur.execute("UPDATE Recommendation SET Type=?, Name=? ,Description=?, Rating=? WHERE RecommendationID=?",
                                                (new_type, new_name, new_desc, new_rtng, rcmd_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")
                    
                    st.markdown("---")
                    formbtn16 = st.button("update Activity")

                    if "formbtn16_state" not in st.session_state:
                        st.session_state.formbtn16_state = False

                    if formbtn16 or st.session_state.formbtn16_state:
                        st.session_state.formbtn16_state = True

                        cur.execute("SELECT ActivityID FROM Activity")
                        act_ids = [row[0] for row in cur.fetchall()]
                        act_id_to_edit = st.selectbox(
                            "Select a ActivityID", act_ids)
                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_activity_data(
                            act_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Activity_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Activity Details:")
                                new_name = st.text_input(
                                    "name", value=existing_data[1])
                                new_desc = st.text_area(
                                    "Description", value=existing_data[2])
                                new_date = st.text_input(
                                    "Date", value=existing_data[3])
                                new_time = st.text_input(
                                    "Time", value=existing_data[4])
                                new_cost = st.text_input(
                                    "Cost", value=existing_data[5])


                                if (st.form_submit_button(label="UPDATE Activity") and new_date and new_name and new_desc and new_time and new_cost):
                                    
                                    cur.execute("UPDATE Activity SET Name=? ,Description=?, Date=?,Time=?,Cost=? WHERE ActivityID=?",
                                                (new_name, new_desc, new_date,str(new_time),new_cost, act_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")
                    
                    st.markdown("---")
                    formbtn17 = st.button("update Weather")

                    if "formbtn17_state" not in st.session_state:
                        st.session_state.formbtn17_state = False

                    if formbtn17 or st.session_state.formbtn17_state:
                        st.session_state.formbtn17_state = True

                        cur.execute("SELECT WeatherID FROM Weather")
                        whtr_ids = [row[0] for row in cur.fetchall()]
                        wthr_id_to_edit = st.selectbox(
                            "Select a WeatherID", whtr_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_weather_data(
                            wthr_id_to_edit)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Weather_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.header("Edit Weather Details:")
                                
                                new_date = st.text_input(
                                    "Date", value=existing_data[1])
                                new_temp = st.text_input(
                                    "Temparture", value=existing_data[2])
                                new_cond = st.text_area(
                                    "Conditions", value=existing_data[3])

                                if (st.form_submit_button(label="UPDATE Weather") and new_date and new_temp and new_cond):
                                   
                                    cur.execute("UPDATE Weather SET Date=? ,Temp=?, Conditions=? WHERE WeatherID=?",
                                                (new_date, new_temp, new_cond ,wthr_id_to_edit))
                                    con.commit()
                                    st.success("Successfully updated!!")


                def render_delete():
                    st.title("To delete values from DB")
                    st.write("Welcome to Page 4.")
                    st.write("Explore and enjoy your stay!")
                    
                    
                    formbtn21 = st.button("Delete a Trip")

                    if "formbtn21_state" not in st.session_state:
                        st.session_state.formbtn21_state = False

                    if formbtn21 or st.session_state.formbtn21_state:
                        st.session_state.formbtn21_state = True

                        cur.execute("SELECT TripID FROM trip")
                        trip_ids = [row[0] for row in cur.fetchall()]
                        trip_id_to_del = st.selectbox(
                            "Select a TripID", trip_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_trip_data(trip_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='trip_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Deleting Trip Details:")
                                st.write(
                                    "Name :",existing_data[1])
                                st.write("Start Month:",existing_data[2])
                                st.write(
                                    "End Month:", existing_data[3])
                                st.write(
                                    "Description:", existing_data[4])
                                st.write(
                                    "Budget:", existing_data[5])
                                if (st.form_submit_button(label="Del Trip") and trip_id_to_del):
                                    cur.execute("DELETE FROM trip WHERE TripID = ?", (trip_id_to_del,))
        
        # Commit the changes to the database
                                    con.commit()
                                    
                                    st.success(f"Trip with ID {trip_id_to_del} deleted successfully!")
                    
                    st.markdown("---")
                    formbtn22 = st.button("Delete Destination")

                    if "formbtn22_state" not in st.session_state:
                        st.session_state.formbtn22_state = False

                    if formbtn22 or st.session_state.formbtn22_state:
                        st.session_state.formbtn22_state = True

                        cur.execute("SELECT DestinationID FROM Destination")
                        dest_ids = [row[0] for row in cur.fetchall()]
                        dest_id_to_del = st.selectbox(
                            "Select a DestinationID", dest_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_dest_data(dest_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='dest_DElETE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Deleting Destination Details:")
                                st.write(
                                    "Destination Name :", existing_data[2])
                                st.write(
                                    "country :",existing_data[3])
                                st.write(
                                    "city :", existing_data[4])
                                st.write(
                                    "Description :",existing_data[5])

                                if (st.form_submit_button(label="Del Dest") and dest_id_to_del):
                                    cur.execute(
                                        "DELETE FROM Destination WHERE DestinationID = ?", (dest_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {dest_id_to_del} deleted successfully!")
                    st.markdown("---")
                    formbtn23 = st.button("DELETE Accommodation")

                    if "formbtn23_state" not in st.session_state:
                        st.session_state.formbtn23_state = False

                    if formbtn23 or st.session_state.formbtn23_state:
                        st.session_state.formbtn23_state = True

                        cur.execute("SELECT AccomodationID FROM Accomodation")
                        acmd_ids = [row[0] for row in cur.fetchall()]
                        accmd_id_to_del = st.selectbox(
                            "Select a AccommodationID", acmd_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_accmd_data(accmd_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='dest_DELETE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Deleting Accommodation Details:")
                                st.write(
                                    "Accomodation Name :",existing_data[2])
                                st.write(
                                    "type :", existing_data[3])
                                st.write(
                                    "Location :", existing_data[4])
                                st.write(
                                    "cost :", value=existing_data[5])

                                if (st.form_submit_button(label="DELETE Accmd") and accmd_id_to_del):
                                    cur.execute(
                                        "DELETE FROM Accomodation WHERE AccomodationID = ?", (accmd_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {accmd_id_to_del} deleted successfully!")
                    st.markdown("---")
                    formbtn24 = st.button("Del a Transportation")

                    if "formbtn24_state" not in st.session_state:
                        st.session_state.formbtn24_state = False

                    if formbtn24 or st.session_state.formbtn24_state:
                        st.session_state.formbtn24_state = True

                        cur.execute("SELECT TransportID FROM Transportation")
                        transp_ids = [row[0] for row in cur.fetchall()]
                        transport_id_to_del = st.selectbox(
                            "Select a TransportID", transp_ids)

                        # Fetch existing data for the specified trip_id
                        existing_data = fetch_transport_data(
                            transport_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Transport_DELETE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Deleting Transport Details:")
                                st.write(
                                    "mode :", existing_data[1])
                                st.write(
                                    "Departure Date time :", existing_data[2])
                                st.write(
                                    "Arrival Date time :", existing_data[3])
                                st.write(
                                    "Departure Location :", existing_data[4])
                                st.write(
                                    "Arrival Location :", existing_data[5])
                                st.write(
                                    "Cost :", existing_data[6])
                                if (st.form_submit_button(label="DELETE Transport") and transport_id_to_del):
                                    cur.execute(
                                        "DELETE FROM Transportation WHERE TransportID = ?", (transport_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {transport_id_to_del} deleted successfully!")
                    st.markdown("---")
                    formbtn25 = st.button("DELETE Recommendation")

                    if "formbtn25_state" not in st.session_state:
                        st.session_state.formbtn25_state = False

                    if formbtn25 or st.session_state.formbtn25_state:
                        st.session_state.formbtn25_state = True

                        cur.execute(
                            "SELECT RecommendationID FROM Recommendation")
                        rcmd_ids = [row[0] for row in cur.fetchall()]
                        rcmd_id_to_del = st.selectbox(
                            "Select a RecommendationID", rcmd_ids)
                        existing_data = fetch_recommendation_data(
                            rcmd_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Recommendation_UPDATE'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Deleting Recommendation Details:")
                                st.write(
                                    "Type :", existing_data[1])
                                st.write(
                                    "Name :", existing_data[2])
                                st.write(
                                    "Description :", existing_data[3])
                                st.write(
                                    "Rating :", existing_data[4])

                                if (st.form_submit_button(label="Delete Recommendation") and rcmd_id_to_del):
                                    cur.execute(
                                        "DELETE FROM Recommendation WHERE RecommendationID = ?", (rcmd_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {rcmd_id_to_del} deleted successfully!")
                    
                    st.markdown("---")
                    formbtn26 = st.button("Delete Activity")

                    if "formbtn26_state" not in st.session_state:
                        st.session_state.formbtn26_state = False

                    if formbtn26 or st.session_state.formbtn26_state:
                        st.session_state.formbtn26_state = True

                        cur.execute("SELECT ActivityID FROM Activity")
                        act_ids = [row[0] for row in cur.fetchall()]
                        act_id_to_del = st.selectbox(
                            "Select a ActivityID", act_ids)
                        existing_data = fetch_activity_data(
                            act_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Activity_Delete'):
                                # Display a form with input fields pre-filled with existing values
                                st.subheader("Edit Activity Details:")
                                st.write(
                                    "name :",existing_data[1])
                                st.write(
                                    "Description :", existing_data[2])
                                st.write(
                                    "Date :", existing_data[3])
                                st.write(
                                    "Time :", existing_data[4])
                                st.write(
                                    "Cost :", existing_data[5])

                                if (st.form_submit_button(label="DELETE Activity") and act_id_to_del):

                                    cur.execute(
                                        "DELETE FROM Activity WHERE ActivityID = ?", (act_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {act_id_to_del} deleted successfully!")

                    st.markdown("---")
                    formbtn27 = st.button("Delete Weather")

                    if "formbtn27_state" not in st.session_state:
                        st.session_state.formbtn27_state = False

                    if formbtn27 or st.session_state.formbtn27_state:
                        st.session_state.formbtn27_state = True

                        cur.execute("SELECT WeatherID FROM Weather")
                        whtr_ids = [row[0] for row in cur.fetchall()]
                        wthr_id_to_del = st.selectbox(
                            "Select a WeatherID", whtr_ids)

                        existing_data = fetch_weather_data(
                            wthr_id_to_del)

                        if existing_data:
                            # Display the existing dat
                            with st.form(key='Weather_delete'):
                                # Display a form with input fields pre-filled with existing values
                                st.header("Deleting Weather Details:")

                                st.write(
                                    "Date :", existing_data[1])
                                st.write(
                                    "Temparture :", existing_data[2])
                                st.write(
                                    "Conditions :", existing_data[3])

                                if (st.form_submit_button(label="Delete Weather") and wthr_id_to_del):

                                    cur.execute(
                                        "DELETE FROM Weather WHERE WeatherID = ?", (wthr_id_to_del,))

                                    con.commit()
                                    st.success(
                                        f"Destination with ID {wthr_id_to_del} deleted successfully!")

                def render_alter():
                    st.title("Alter Page -to alter tables")
                    st.write("Welcome to the Alter Page!")
                    st.write("Click on the sidebar to navigate to other pages.")

                    formbtn31 = st.button("Alter trip")

                    if "formbtn31_state" not in st.session_state:
                        st.session_state.formbtn31_state = False

                    if formbtn31 or st.session_state.formbtn31_state:
                        st.session_state.formbtn31_state = True

                        st.title("Alter Trip Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                                        'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input("Enter new column name:")
                            new_column_type = st.text_input("Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE trip ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input("Enter column name to modify:")
                            new_data_type = st.text_input("Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE trip DROP COLUMN {column_to_modify};")
                                    cur.execute(
                                        
                                        f"ALTER TABLE trip ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input("Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(f"ALTER TABLE trip DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error dropping column: {str(e)}")

                    st.markdown("---")

                    formbtn32 = st.button("Alter Destination")

                    if "formbtn32_state" not in st.session_state:
                        st.session_state.formbtn32_state = False

                    if formbtn32 or st.session_state.formbtn32_state:
                        st.session_state.formbtn32_state = True

                        st.title("Alter Destination Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Destination ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Destination DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Destination ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Destination DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")
                                    
                    st.markdown("---")

                    formbtn33 = st.button("Alter Accommodation")

                    if "formbtn33_state" not in st.session_state:
                        st.session_state.formbtn33_state = False

                    if formbtn33 or st.session_state.formbtn33_state:
                        st.session_state.formbtn33_state = True

                        st.title("Alter Accommodation Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Accomodation ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Accomodation DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Accomodation ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Accomodation DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")

                    st.markdown("---")

                    formbtn34 = st.button("Alter Transportation")

                    if "formbtn34_state" not in st.session_state:
                        st.session_state.formbtn34_state = False

                    if formbtn34 or st.session_state.formbtn34_state:
                        st.session_state.formbtn34_state = True

                        st.title("Alter Transportation Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Transportation ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Transportation DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Transportation ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Transportation DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")
                                    
                    st.markdown("---")
                    formbtn35 = st.button("Alter Recommendation")

                    if "formbtn35_state" not in st.session_state:
                        st.session_state.formbtn35_state = False

                    if formbtn35 or st.session_state.formbtn35_state:
                        st.session_state.formbtn35_state = True

                        st.title("Alter Recommendation Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Recommendation ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Recommendation DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Recommendation ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Recommendation DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")
                                    
                    st.markdown("---")

                    formbtn36 = st.button("Alter Activity")

                    if "formbtn36_state" not in st.session_state:
                        st.session_state.formbtn36_state = False

                    if formbtn36 or st.session_state.formbtn36_state:
                        st.session_state.formbtn36_state = True

                        st.title("Alter Accommodation Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Activity ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Activity DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Activity ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Activity DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")
                    st.markdown("---")

                    formbtn37 = st.button("Alter Weather")

                    if "formbtn37_state" not in st.session_state:
                        st.session_state.formbtn37_state = False

                    if formbtn37 or st.session_state.formbtn37_state:
                        st.session_state.formbtn37_state = True

                        st.title("Alter Weather Table")

    # Get user input on the action to perform
                        action = st.radio("Select action:", [
                            'Add Column', 'Modify Column', 'Drop Column'])

                        if action == 'Add Column':
                            new_column_name = st.text_input(
                                "Enter new column name:")
                            new_column_type = st.text_input(
                                "Enter new column data type:")
                            if st.button("Add Column"):
                                try:
                                    # Execute SQL to add a new column
                                    cur.execute(
                                        f"ALTER TABLE Weather ADD COLUMN {new_column_name} {new_column_type};")
                                    con.commit()
                                    st.success(
                                        f"Column {new_column_name} added successfully!")
                                except sqlite3.Error as e:
                                    st.error(f"Error adding column: {str(e)}")

                        elif action == 'Modify Column':
                            column_to_modify = st.text_input(
                                "Enter column name to modify:")
                            new_data_type = st.text_input(
                                "Enter new data type:")
                            if st.button("Modify Column"):
                                try:
                                    # Execute SQL to modify a column's data type
                                    cur.execute(
                                        f"ALTER TABLE Weather DROP COLUMN {column_to_modify};")
                                    cur.execute(

                                        f"ALTER TABLE Weather ADD COLUMN {column_to_modify} {new_data_type};")
                                    st.success(
                                        f"Column {column_to_modify} modified successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error modifying column: {str(e)}")

                        elif action == 'Drop Column':
                            column_to_drop = st.text_input(
                                "Enter column name to drop:")
                            if st.button("Drop Column"):
                                try:
                                    # Execute SQL to drop a column
                                    cur.execute(
                                        f"ALTER TABLE Weather DROP COLUMN {column_to_drop};")
                                    con.commit()
                                    st.success(
                                        f"Column {column_to_drop} dropped successfully!")
                                except sqlite3.Error as e:
                                    st.error(
                                        f"Error dropping column: {str(e)}")


                    st.markdown("---")

                    formbtn41 = st.button("Datatype")
                    if "formbtn41_state" not in st.session_state:
                        st.session_state.formbtn41_state = False

                    if formbtn41 or st.session_state.formbtn41_state:
                        st.session_state.formbtn41_state = True

                        table_name = st.text_input("Enter Table Name :")
                        column_name = st.text_input("Enter Col Name :")

                        if(table_name and column_name):
    # Execute the PRAGMA statement to get column information
                            cur.execute(f"PRAGMA table_info({table_name})")

        # Fetch all rows from the result set
                            columns_info = cur.fetchall()

        # Find the datatype of the specified column
                            datatype = None
                            for column_info in columns_info:
                                if column_info[1] == column_name:
                                    datatype = column_info[2]
                                    break

                                # Display the datatype
                            if datatype is not None:
                                st.write(
                                    f"The datatype of column '{column_name}' in table '{table_name}' is: {datatype}")
                            else:
                                st.write(
                                    f"Column '{column_name}' not found in table '{table_name}'")

                def main():
                    st.sidebar.title("Navigation")

                    selected_page = st.sidebar.radio(
                        "Select a Page", ["Home", "create", "read", "update", "delete","alter"])
                    if selected_page == "Home":
                        render_home()
                    elif selected_page == "create":
                        render_create()
                    elif selected_page == "read":
                        render_read()
                    elif selected_page == "update":
                        render_update()
                    elif selected_page == "delete":
                        render_delete()
                    elif selected_page == "alter":
                        render_alter()

                if __name__ == "__main__":
                    main()

                    st.markdown("---")
                    st.write("© 2023 Trip Planner App. All rights reserved.")

                elif not authentication_status:
                    with info:
                        st.error('Incorrect Password or username')
                else:
                    with info:
                        st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')


except:
    st.success('Refresh Page')