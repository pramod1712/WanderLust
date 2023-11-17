import streamlit as st
import streamlit_authenticator as stauth
from dependancies_admin import sign_up, fetch_users
import sqlite3

try:
    con = sqlite3.connect('trip_planner2.db')
    cur = con.cursor()
    print("connected")
    #con = st.connection('trip_planner2', type='sql')
except:
    st.error("could not connect to database")

st.set_page_config(page_title='WanderLust Admin', page_icon='🦸‍♂️', initial_sidebar_state='expanded')
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
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='TripPlannerAdmin', key='abcdef', cookie_expiry_days=1)

    email, authentication_status, username = Authenticator.login(':orange[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome Admin {username}')
                Authenticator.logout('Log Out', 'sidebar')

                #st.title("WanderLust Admin Panel")

                # Fetch data from the 'trip' table

                #trip_data = con.execute('select TripName from trip').fetchall()

                # Extract the TripName values from the result set
                #trip_names = [row[0] for row in trip_data]
                
                st.write("view info about the trips")
                trip_table = cur.execute('select * from trip')
                st.dataframe(trip_table)
                st.write("displayed table")

                st.write("view info about the destination")
                dest_table = cur.execute('select * from destination')
                st.dataframe(dest_table)
                st.write("displayed table")

                if st.button("Edit"):
                    st.success(
                        f"changes made")


                st.info("Modify the trips according to your heart!")

                st.markdown("---")
                st.write("© 2023 Trip Planner App. All rights reserved.")

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
