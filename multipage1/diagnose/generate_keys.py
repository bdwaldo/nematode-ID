import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Benjamin"]
usernames = ["nema-guy"]
passwords = [""]

hashed_passwords = stauth.Hasher(passwords).generate()

#create pickle file and save information
file_path = /diagnose / "hashed_pw.pkl"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords, file)
 
