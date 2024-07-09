#login page
#https://pypi.org/project/streamlit-authenticator/

import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
    
#Creating a login widget
with open('multipage1/diagnose/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()
#name, authentication_status, username = authenticator.login('Login', 'main')

#Authenticating users



if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')


#Creating a reset password widget
#if st.session_state["authentication_status"]:
#    try:
#        if authenticator.reset_password(st.session_state["username"]):
#            st.success('Password modified successfully')
#    except Exception as e:
#        st.error(e)





#Creating a new user registration widget
#try:
#    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
#    if username_of_forgotten_password:
#        st.success('New password to be sent securely')
#        # The developer should securely transfer the new password to the user.
#    elif username_of_forgotten_password == False:
#        st.error('Username not found')
#except Exception as e:
#    st.error(e)


#Creating a forgot password widget
#if st.session_state["authentication_status"]:
#    try:
#        if authenticator.update_user_details(st.session_state["username"]):
#            st.success('Entries updated successfully')
#    except Exception as e:
#        st.error(e)

#Creating a forgot username widget
#with open('../config.yaml', 'w') as file:
#    yaml.dump(config, file, default_flow_style=False)
