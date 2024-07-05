#https://www.youtube.com/watch?v=JoFGrSRj4X4
#import pickle
#from pathlib import Path

#import streamlit_authenticator as stauth

#names = ["Benjamin"]
#usernames = ["nema-guy"]

#load hashed passwords
#file_path = Path(_file_).Parent / "hashed_pw.pkl"
#with file_path.open("rb") as file: #open with root binary mode
#    hased_passwords = pickle.load(file) #load pickle file

#create authenticator object
#authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
#                                    "nema-ID", "4fet", cookie_expiry_days=1) #cookie

#name, authentication_status, username = authenticator.login("Login", "main")

#authentication status
#if authentication_status == False: 
#    st.error("Username/password is incorrent")

if authentification_status == None:
    st.warning("Please enter your uername and password")

authenticator.logout("Logout", "sidebar")
st.sidebar.title(f"Welcome {name}")
