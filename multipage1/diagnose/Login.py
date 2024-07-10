#login page
#https://pypi.org/project/streamlit-authenticator/
  
import streamlit as st
import streamlit_authenticator as stauth

def sign_up():
  with st.form(key='signup', clear_on_submit = True):
    st.subheader('Create account')
    email = st.text_input('Email', placeholder='Enter your email')
    name = st.text_input('Name', placeholder='Enter your name')
    organization = st.text_input('Organization', placeholder='Enter your organization')
    password1 = st.text_input('Password', placeholder='Enter your password')
    password2 = st.text_input('Confirm Password', placeholder='Confirm password')
  
    if email:
      if validate_email(email):
        if email not in get_user_emails():
          if validate_username(username):
            if username not in get_usernames():
              if password1 == password2:
                hashed_password = stauth.Hasher([password2]).generate #add user to database
                insert_user(email, username, hashed_password[0])
                st.success('Account created successfully')
              else:
                st.warning('Passwords do not match')
            else:
              st.warning('Username Already Exists')
          else:
            st.warning('Invalid Username')
        else:
          st.warning('Invalid Email')
  st.form_submit_button('Sign Up')  

sign_up()

                   
                   
            


            
      
  
