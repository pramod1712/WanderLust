import sqlite3

con = sqlite3.connect('trip_plannerr1.db')
cur = con.cursor()

# add attribute to store user's country - to adjust prices, currencies
cur.execute('''
CREATE TABLE IF NOT EXISTS User (
  Username TEXT PRIMARY KEY,
  Email TEXT UNIQUE NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Trip (
  TripID TEXT PRIMARY KEY,
  TripName TEXT NOT NULL,
  RecommendedStartMonth TEXT,
  RecommendedEndMonth TEXT,
  Description TEXT,
  Budget NUMERIC(10,2)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Destination (
  TripID TEXT,
  DestinationID TEXT PRIMARY KEY,
  Name TEXT NOT NULL,
  Country TEXT NOT NULL,
  City TEXT NOT NULL,
  Description TEXT,
  foreign key (TripID) references Trip(TripID) 
)
''')


cur.execute('''
CREATE TABLE IF NOT EXISTS Accomodation (
  TripID TEXT,
  AccomodationID TEXT PRIMARY KEY,
  Name TEXT NOT NULL,
  Type TEXT NOT NULL,
  Location TEXT NOT NULL,
  Cost NUMERIC(10,2),
  foreign key (TripID) references Trip(TripID) 
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Transportation (
            
  TransportID TEXT PRIMARY KEY,
  Mode TEXT NOT NULL,
  DepartureDatetime DATETIME NOT NULL,
  ArrivalDatetime DATETIME NOT NULL,
  DepartureLocation TEXT NOT NULL,
  ArrivalLocation TEXT NOT NULL,
  Cost NUMERIC(10,2)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Recommendation (
  RecommendationID TEXT PRIMARY KEY,
  Type TEXT NOT NULL,
  Name TEXT NOT NULL,
  Description TEXT,
  Rating NUMERIC(2,1)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Activity (
  ActivityID  TEXT PRIMARY KEY,
  Name TEXT NOT NULL,
  Description TEXT,
  Date DATE NOT NULL,
  Time TIME NOT NULL,
  Cost NUMERIC(10,2)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Weather (
  WeatherID TEXT PRIMARY KEY,
  Date DATE,
  Temp NUMERIC(3,1),
  Conditions TEXT
)
''')

