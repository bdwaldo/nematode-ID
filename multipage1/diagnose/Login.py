#login page
#https://pypi.org/project/streamlit-authenticator/
  
import streamlit as st
import streamlit_authenticator as stauth


with st.form(key='signup', clear_on_submit = True):
  st.subheader('Sign Up')
  email = st.text_input('Email', placeholder='Enter your email')
  name = st.text_input('Name', placeholder='Enter your name')
  password1 = st.text_input('Password', placeholder='Enter your password')
  password2 = st.text_input('Confirm Password', placeholder='Confirm password')
  st.form_submit_button('Sign Up')
  
  
