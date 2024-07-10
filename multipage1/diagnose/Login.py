#login page
#https://pypi.org/project/streamlit-authenticator/
  
import streamlit as st
import streamlit_authenticator as stauth

def sign_up():
  with st.form(key='signup', slear_on_submit = True):
    at.subheader('Sign Up')
