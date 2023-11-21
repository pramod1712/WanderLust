import streamlit as st
import streamlit_authenticator as stauth
from dependancies_admin import sign_up, fetch_users
import sqlite3


    

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

                def render_create():
                    st.title("Page 1")
                    st.write("This is Page 1.")
                    st.write("Feel free to explore!")
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
                            if submit_form: 
                                
                                if activity_id and name and description and date and time and cost:
                                # Insert the new activity into the database
                                    cur.execute(
                                        "insert into Activity (ActivityID,Name,Description,Date,Time,Cost) values (?,?,?,?,?,?)",(activity_id,name,description,date,time,cost))
                                    
                                    con.commit()
                                    st.success("Activity added successfully!")
                        
                        
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

                def render_home():
                    st.title("Home Page")
                    st.write("Welcome to the Home Page!")
                    st.write("Click on the sidebar to navigate to other pages.")
                    cur = con.cursor()

                
                    

                def render_read():
                    st.title("Page 2")
                    st.write("You've reached Page 2.")
                    st.write("Navigate around and enjoy!")
                    if (st.button("display trips")):
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
                    formbtn = st.button("update a New Trip")

                    if "formbtn_state" not in st.session_state:
                        st.session_state.formbtn_state = False

                    if formbtn or st.session_state.formbtn_state:
                        st.session_state.formbtn_state = True

                        st.subheader("Trip Information Form")

                        with st.form(key='trip_info'):
                            st.write('New Trip')

                            #trip_id = st.text_input(label="Trip ID")
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
                                if trip_name and start_month and end_month and description and budget:
                                    # Insert user information into the Trip table
                                    
                                    
                                    cur.execute(
    "UPDATE Trip SET TripName = ?, RecommendedStartMonth = ?, RecommendedEndMonth = ?, Description = ?, Budget = ? WHERE TripID = 1",
    (trip_name, start_month, end_month, description, budget)
)
                                    con.commit()

                                    st.success(
                                            f"Trip registered successfully!")
                                    
                                else:
                                    st.warning(
                                        "Please fill all the fields in the form.")
                def render_delete():
                    st.title("Page 4")
                    st.write("Welcome to Page 4.")
                    st.write("Explore and enjoy your stay!")

                def main():
                    st.sidebar.title("Navigation")

                    selected_page = st.sidebar.radio(
                        "Select a Page", ["Home", "create", "read", "update", "delete"])
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