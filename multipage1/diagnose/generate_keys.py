#https://www.youtube.com/watch?v=JoFGrSRj4X4
import pickle
from pathlib import Path
from streamlit_authenticator.utilities import hasher

import streamlit_authenticator as stauth

names = ["Benjamin"]
usernames = ["nema-guy"]
passwords = ["XXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

create pickle file and save information
file_path = Path(_file_).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords, file)
 
