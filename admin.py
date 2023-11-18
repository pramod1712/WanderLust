import streamlit as st
import streamlit_authenticator as stauth
from dependancies_admin import sign_up, fetch_users
import sqlite3

def add_transportation():
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
        cost = st.number_input("Cost", value=0.0)

        # Check if all fields are filled
        if st.form_submit_button("Submit") and all([transport_id, mode, departure_datetime, arrival_datetime, departure_location, arrival_location, cost]):
            # Insert the new transportation into the database
            cur.execute(
                "INSERT INTO Transportation (TransportID, Mode, DepartureDatetime, ArrivalDatetime, DepartureLocation, ArrivalLocation, Cost) VALUES (?, ?, ?, ?, ?, ?, ?);",
                (transport_id, mode, departure_datetime, arrival_datetime, departure_location, arrival_location, cost)
            )
            con.commit()
            st.success("Transportation added successfully!")


try:
    con = sqlite3.connect('trip_planner2.db')
    cur = con.cursor()
    print("connected")
    # con = st.connection('trip_planner2', type='sql')
except:
    st.error("could not connect to database")

st.set_page_config(page_title='WanderLust Admin',
                   page_icon='🦸‍♂️', initial_sidebar_state='expanded')
st.title("WanderLust Admin Panel")

try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
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
                                    cur.execute(
                                        "INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES (?, ?, ?, ?, ?, ?)",
                                        (trip_id, trip_name, start_month, end_month, description, budget)
                                    )
                                    con.commit()
                                    st.success(f"Trip registered successfully!")
                                    trip_table = cur.execute('select * from trip')
                                    st.dataframe(trip_table)
                                except sqlite3.IntegrityError:
                                    st.warning("TripID already exists, please use a different ID.")
                            else:
                                st.warning("Please fill all the fields in the form.")

                if (st.button("New Destination")):
                    st.subheader("Add a New Destination")
                    with st.form(key='add_destination_form'):
                    # Collect destination details from the user
                        trip_id = st.text_input("Trip ID")
                        destination_id = st.text_input("Destination ID")  # Limit the length if needed
                        name = st.text_input("Name")  # Adjust the maximum length accordingly
                        country = st.text_input("Country")
                        city = st.text_input("City")
                        description = st.text_area("Description")

                        # Check if all fields are filled
                        if st.form_submit_button("Submit") and all([trip_id, destination_id, name, country, city]):
                                    # Insert the new destination into the database
                                    cur.execute(
                                        "INSERT INTO Destination (TripID, DestinationID, Name, Country, City, Description) VALUES (?, ?, ?, ?, ?, ?);",
                                        (trip_id, destination_id, name, country, city, description)
                                    )
                                    con.commit()
                        
                                    st.success("Destination added successfully!")
                
                if (st.button("New transportation")):
                    add_transportation()

                if (st.button("New accodimation")):
                       
                    st.subheader("Add New Accommodation")

                    # Create a form
                    with st.form(key='add_accommodation_form'):
                        # Collect accommodation details from the user
                        trip_id = st.text_input("Trip ID")
                        accommodation_id = st.text_input("Accommodation ID")
                        name = st.text_input("Name")
                        accommodation_type = st.text_input("Type")
                        location = st.text_input("Location")
                        cost = st.number_input("Cost")

                        # Check if all fields are filled
                        if st.form_submit_button("Submit") and all([trip_id, accommodation_id, name, accommodation_type, location]):
                            # Insert the new accommodation into the database
                            cur.execute(
                                "INSERT INTO Accommodation (TripID, AccommodationID, Name, Type, Location, Cost) VALUES (?, ?, ?, ?, ?, ?);",
                                (trip_id, accommodation_id, name, accommodation_type, location, cost)
                            )
                            con.commit()
                            st.success("Accommodation added successfully!")

                if (st.button("New recommendation")):
                        st.subheader("Add New Recommendation")

                                    # Create a form
                        with st.form(key='add_recommendation_form'):
                                        # Collect recommendation details from the user
                            recommendation_id = st.text_input("Recommendation ID")
                            recommendation_type = st.text_input("Type")
                            name = st.text_input("Name")
                            description = st.text_area("Description")
                            rating = st.number_input("Rating")

                                        # Check if all fields are filled
                            if st.form_submit_button("Submit") and all([recommendation_id, recommendation_type, name]):
                                            # Insert the new recommendation into the database
                                cur.execute("INSERT INTO Recommendation (RecommendationID, Type, Name, Description, Rating) VALUES (?, ?, ?, ?, ?);",(recommendation_id, recommendation_type, name, description, rating))
                                con.commit()
                                st.success("Recommendation added successfully!")

                if(st.button("New activity")):
                                st.subheader("Add New Activity")

                                    # Create a form
                                with st.form(key='add_activity_form'):
                                        # Collect activity details from the user
                                        activity_id = st.text_input("Activity ID")
                                        name = st.text_input("Name")
                                        description = st.text_area("Description")
                                        date = st.date_input("Date")
                                        time = st.time_input("Time")
                                        cost = st.number_input("Cost", value=0.0)

                                        # Check if all fields are filled
                                        if st.form_submit_button("Submit") and all([activity_id, name, date, time]):
                                            # Insert the new activity into the database
                                            cur.execute(
                                                "INSERT INTO Activity (ActivityID, Name, Description, Date, Time, Cost) VALUES (?, ?, ?, ?, ?, ?);",
                                                (activity_id, name, description, date, time, cost)
                                            )
                                            con.commit()
                                            st.success("Activity added successfully!")

                                            st.subheader("Add New Weather Details")
                if(st.button("new weather")):
                            st.subheader("Add New weather")
                            # Create a form
                            with st.form(key='add_weather_form'):
                                # Collect weather details from the user
                                weather_id = st.text_input("Weather ID")
                                date = st.date_input("Date")
                                temp = st.number_input("Temperature", value=0.0, step=0.1)
                                conditions = st.text_input("Conditions")

                                # Check if all fields are filled
                                if st.form_submit_button("Submit") and all([weather_id, date, temp, conditions]):
                                    # Insert the new weather details into the database
                                    cur.execute(
                                        "INSERT INTO Weather (WeatherID, Date, Temp, Conditions) VALUES (?, ?, ?, ?);",
                                        (weather_id, date, temp, conditions)
                                    )
                                    con.commit()
                                    st.success("Weather details added successfully!")

                
                
                def render_home():
                    st.title("Home Page")
                    st.write("Welcome to the Home Page!")
                    st.write("Click on the sidebar to navigate to other pages.")
                    cur = con.cursor()

                    
                def render_create():
                    st.title("Page 1")
                    st.write("This is Page 1.")
                    st.write("Feel free to explore!")
                    if(st.button("New trip")):
                        st.subheader("Add a New Trip")

                        # Create a form
                        with st.form(key='add_trip_form'):
                            # Collect trip details from the user
                            trip_id = st.text_input("Trip ID")
                            trip_name = st.text_input("Trip Name")
                            start_month = st.text_input("Recommended Start Month")
                            end_month = st.text_input("Recommended End Month")
                            description = st.text_area("Description")
                            budget = st.number_input("Budget")

                            # Check if all fields are filled
                            
                            
                            if (st.form_submit_button("Submit")):
                                # Insert the new trip into the database
                                        cur.execute(
                                    "INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES (?, ?, ?, ?, ?, ?)",(trip_id, trip_name, start_month, end_month, description, budget))
                                        con.commit()
                                        st.success("Trip added successfully!")
                        if(st.button("sun")):
                                cur.execute(
                                    "INSERT INTO Trip (TripID, TripName, RecommendedStartMonth, RecommendedEndMonth, Description, Budget) VALUES (?, ?, ?, ?, ?, ?)", (trip_id, trip_name, start_month, end_month, description, budget))

                                con.commit()
                def render_read():
                    st.title("Page 2")
                    st.write("You've reached Page 2.")
                    st.write("Navigate around and enjoy!")
                    if(st.button("display trips")):
                        st.write("view info about the trips")
                        trip_table = cur.execute('select * from trip')
                        st.dataframe(trip_table)

                    if (st.button("display destinations")):
                        st.write("view info about the destinations")
                        trip_table = cur.execute('select * from Destination')
                        st.dataframe(trip_table)

                    if (st.button("display Accomodations")):
                        st.write("view info about the Accomodations")
                        trip_table = cur.execute('select * from Accomodation')
                        st.dataframe(trip_table)
                        st.write("displayed table")
                    if (st.button("display Transportation")):
                        st.write("view info about the Transportation")
                        trip_table = cur.execute(
                            'select * from Transportation')
                        st.dataframe(trip_table)
                        st.write("displayed table")
                    if (st.button("display Recommendation")):
                        st.write("view info about the Recommendation")
                        trip_table = cur.execute(
                            'select * from Recommendation')
                        st.dataframe(trip_table)
                        st.write("displayed table")
                    if (st.button("display Activity")):
                        st.write("view info about the Activity")
                        trip_table = cur.execute('select * from Activity')
                        st.dataframe(trip_table)
                        st.write("displayed table")
                    if (st.button("display Weather")):
                        st.write("view info about the Weather")
                        trip_table = cur.execute('select * from Weather')
                        st.dataframe(trip_table)
                        st.write("displayed table")

                def render_update():
                    st.title("Page 3")
                    st.write("This is Page 3.")
                    st.write("Have a great time here!")


                def render_delete():
                    st.title("Page 4")
                    st.write("Welcome to Page 4.")
                    st.write("Explore and enjoy your stay!")


                def main():
                    st.sidebar.title("Navigation")
                    
                    selected_page = st.sidebar.radio("Select a Page", ["Home", "create", "read","update","delete"])
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