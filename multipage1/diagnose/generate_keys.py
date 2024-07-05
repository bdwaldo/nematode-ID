import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Benjamin"]
usernames = ["nema-guy"]
passwords = ["XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

#create pickle file and save information
file_path = Path(_file_).parent / "hashed_pw.pkl"
with file_path.open("nb") as file:
  pickle.dump(hashed_passwords, file)
 
