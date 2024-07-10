#login page
#https://pypi.org/project/streamlit-authenticator/
  
import streamlit as st
import streamlit_authenticator as stauth


with st.form(key='signup', clear_on_submit = True):
  st.subheader('Sign Up')
  st.form_submit_button('Sign Up')
