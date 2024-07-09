#login page
#https://pypi.org/project/streamlit-authenticator/

import streamlit as st
import streamlit_authenticator as sa
  
auth = sa.Authenticator(
    SECRET_KEY,
    token_url="/token",
    token_ttl=3600,
    password_hashing_method=sa.PasswordHashingMethod.BCRYPT,
)


@auth.login_required
def protected():
    st.write("This is a protected route.")



@st.route("/login")
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
 
    if st.button("Login"):
        user = auth.authenticate(username, password)
        if user is not None:
            auth.login_user(user)
            st.success("Logged in successfully.")
        else:
            st.error("Invalid username or password.")



## .streamlit/secrets.toml
password = "streamlit123"



password = st.text_input("Password", type="password")
 
if password == st.secrets["password"]:
    st.success("Access granted.")
else:
    st.error("Access denied.")
