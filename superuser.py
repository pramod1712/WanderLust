import streamlit as st
import streamlit_authenticator as stauth
import datetime
from deta import Deta

# Deta keys
DETA_KEY_CLIENT = 'd0dcu4dmndq_wYDzZtDV5VHNrqrbrZYpGF6TH5H9vphv'
DETA_KEY_ADMIN = 'd029nxxjmxf_f592BNXFs8XV33y7fDgyGYNi3XtWJckT'

# Initialize Deta bases
deta = Deta(DETA_KEY_CLIENT)
db = deta.Base('StreamlitAuth')

deta2 = Deta(DETA_KEY_ADMIN)
admin_db = deta2.Base('Admin_Creds')

# Authentication
#stauth.set_config(admin_db)
db = deta.Base('StreamlitAuth')

# Check if the user is authenticated
if not db:
    st.write("Not authenticated.")
    st.stop()

# Function to insert a new user
def insert_user(email, username, password):
    date_joined = str(datetime.datetime.now())
    return db.put({'key': email, 'username': username, 'password': password, 'date_joined': date_joined})

# Function to fetch all users
def fetch_users():
    users = db.fetch()
    return users.items

# Function to get all user emails
def get_user_emails():
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user['key'])
    return emails

# Function to get all usernames
def get_usernames():
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user['username'])
    return usernames

# Custom alternating color function
def alternating_color(i):
    return "#f0f0f0" if i % 2 == 0 else "#ffffff"

# Streamlit Dashboard
def main():
    st.title("Superuser Dashboard")

    # Display all users with expandable details
    st.header("All Users")
    users = fetch_users()
    if users:
        for i, user in enumerate(users):
            expander_title = f"User: {user['username']}"
            with st.expander(expander_title):
                st.write(f"Username: {user['username']}")
                st.write(f"Email: {user['key']}")
                st.write(f"Date Joined: {user['date_joined']}")

    else:
        st.write("No users found.")

    # Display User Emails and Usernames side by side with alternating colors
    st.header("User Emails and Usernames")

    emails = get_user_emails()
    usernames = get_usernames()

    num_users = max(len(emails), len(usernames))
    for i in range(num_users):
        col1, col2 = st.columns(2)

        if i < len(emails):
            with col1:
                #col1.subheader("User Email")
                col1.text(emails[i])
                col1.write('')  # Add empty space for separation

        if i < len(usernames):
            with col2:
                #col2.subheader("Username")
                col2.text(usernames[i])
                col2.write('')  # Add empty space for separation

    if len(emails) == 0 and len(usernames) == 0:
        st.write("No user emails or usernames found.")

if __name__ == "__main__":
    main()

