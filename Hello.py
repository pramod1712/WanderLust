import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users, get_symbol
import sqlite3
from st_clickable_images import clickable_images
import re
from html.parser import HTMLParser

class NewlineSelectbox:
    def __init__(self, label, options):
        self.label = label
        self.options = options

    def render(self):
        selected_index = st.selectbox(self.label, [option.replace('<br>', '\n') for option in self.options])
        return self.options[selected_index]

#global variables
currency_code = 'INR'

try:
    con = sqlite3.connect('trip_planner2.db')
    cur = con.cursor()
    print("connected")
    #con = st.connection('trip_planner2', type='sql')
except:
    st.error("could not connect to database")

st.set_page_config(page_title='Trip Planner', page_icon='✈', initial_sidebar_state='collapsed')


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
                
                
                # Fetch data from the 'trip' table
                select_trips = "SELECT TripName || '\n' || Description || '\n' || Budget FROM trip;"
                trips_data = cur.execute(select_trips).fetchall()
    
                # Streamlit app
                st.title('Choose your Dream Trip!')

                # Create a selectbox with trip names
                options = []
                try:
                    for row in trips_data:
                        string_to_display = row[0]  # Replace 'column_index' with the actual column index
                        formatted_string = re.sub('\n', '<br>', string_to_display)
                        options.append(int(formatted_string))
                except Exception as e:
                    print(e)

                # Render the selectbox
                #st.info(options)
                #trip_option = st.selectbox('Select a string:', options)
                #trip_option = st.selectbox('Select your dream trip!', trips_data)
                try:
                    # Create an instance of the custom selectbox component
                    newline_selectbox = NewlineSelectbox('Select a string:', options)

                    # Render the custom selectbox component
                    selected_string = newline_selectbox.render()
                    st.write('Selected string:', selected_string)
                except Exception as e:
                    print(e)

                    
                
                """if trip_option:
                        st.title("Your destination options")
                        select_dest = f"select Name, City, Description, Country,  from Destination where Destination.TripID = Trip.TripID"
                """     
                        
                
                
                
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
