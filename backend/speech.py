import pyttsx3

engine=pyttsx3.init()
rate=engine.getProperty("rate")
engine.setProperty('rate',100)
engine.runAndWait()
volume=engine.getProperty("volume")
print("volume is {0}".format(volume))
engine.setProperty("volume",1)
voices=engine.getProperty('voices')
print('Male voice:{0}'.format(voices[0].id))
print('Female voice:{0}'.format(voices[1].id))
engine.setProperty("voice",voices[1].id)
rate=engine.getProperty("rate")
engine.setProperty('rate',180)


welcome_text="""
Wanderluxe, crafted by Pramod S and Kanith Kumar from PES University, Bangalore, 
is your ultimate travel planner. It organizes trips, suggests activities, and manages bookings—all in one app. 
Tailored to your preferences, it recommends personalized options for accommodations, dining, and sightseeing. 
Wanderluxe simplifies bookings and sends real-time updates on itinerary changes. 

It's your digital companion, offering offline maps, destination info, and language translations. 
Whether a weekend escape or a global adventure, Wanderluxe ensures smooth, stress-free travel. 
Join the journey to explore the world effortlessly and make unforgettable memories along the way.
"""

def speak():
    engine.say(welcome_text)
    engine.runAndWait()

