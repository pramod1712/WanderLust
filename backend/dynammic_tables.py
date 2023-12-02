import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users, get_symbol
import sqlite3

table_name = st.text_input(':blue[Table Name]', placeholder='Enter the name of the table')


query = '''
CREATE TABLE IF NOT EXISTS {table_name} (
  TripID TEXT PRIMARY KEY,
  TripName TEXT NOT NULL,
  RecommendedStartMonth TEXT,
  RecommendedEndMonth TEXT,
  Description TEXT,
  Budget NUMERIC(10,2),
  ImageURL TEXT
)
'''