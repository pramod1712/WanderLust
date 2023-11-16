import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users
import sqlite3

try:
    #con = sqlite3.connect('trip_planner2.db')
    #cur = con.cursor()
    con = st.connection('trip_planner2', type='sql')
except:
    st.error("could not connect to database")

st.set_page_config(page_title='Trip Planner', page_icon='🐍', initial_sidebar_state='collapsed')


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

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome {username}')
                Authenticator.logout('Log Out', 'sidebar')

                st.title("Trip Planner and Management System")

                st.write("Plan and manage your trips with ease!")
                
                start_date = st.date_input("Select the start date:")
                end_date = st.date_input("Select the end date:")
                trip_table = con.query('select * from trip')
                st.dataframe(trip_table)

                if st.button("Plan My Trip"):
                    st.success(
                        f"Trip planned from {start_date} to {end_date}")


                st.info("Explore our amazing features and make your trips memorable!")

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


"""
source = st.text_input("Enter your source:", "")
destination = st.text_input("Enter your destination:", "")
"""