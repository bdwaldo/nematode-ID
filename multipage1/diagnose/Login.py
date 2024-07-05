import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Benjamin"]
usernames = ["nema-guy"]

#load hashed passwords
file_path = Path(_file_).Parent / "hashed_pw.pkl
with file_path.open("rb") as file: #open with root binary mode
    hased_passwords = pickle.load(file) #load pickle file

#create authenticator object
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
                                    "nema-ID", "4fet", cookie_expiry_days=1) #cookie

hashed_passwords = stauth.Hasher(passwords).generate()




if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

file_path = Path(_file_).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
  pickle.dump(hashed_passwords, file)
