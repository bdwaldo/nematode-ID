
#streamlit authenticator login
#https://github.com/mkhorasani/Streamlit-Authenticator/tree/main?tab=readme-ov-file#authenticatelogin

import streamlit as st
import streamlit_authenticator as stauth
#from streamlit_extras.switch_page_button import switch_page
import yaml

# Load your configuration file (replace '../config.yaml' with your actual path)
#make sure yaml file extension is correct. won't work if created in jupytr notebook
with open('diagnose/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)


# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)


#this function is the up to date version
authenticator.login()


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
    
    #st.button('Single sample', on_click=st.switch_page('multipage1/diagnose/Single.py'))
    #st.switch_page('diagnose/Single.py') #switch to sample submission page









#reset password
#if st.session_state["authentication_status"]:
#    try:
#        if authenticator.reset_password(st.session_state["username"]):
#            st.success('Password modified successfully')
#    except Exception as e:
#        st.error(e)


#New user
#won't add user to gihub file. need to connect to database
#try:
#    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
#    if email_of_registered_user:
#        st.success('User registered successfully')
#except Exception as e:
#    st.error(e)




#forgot password
#try:
#    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
#    if username_of_forgotten_password:
#        st.success('New password to be sent securely')
#        # The developer should securely transfer the new password to the user.
#    elif username_of_forgotten_password == False:
#        st.error('Username not found')
#except Exception as e:
#    st.error(e)


#forgot username
#try:
#    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
#    if username_of_forgotten_username:
#        st.success('Username to be sent securely')
#        # The developer should securely transfer the username to the user.
#    elif username_of_forgotten_username == False:
#        st.error('Email not found')
#except Exception as e:
#    st.error(e)
    

#####################
#update user information
#have to connect to database to store user info file
#if st.session_state["authentication_status"]:
#    try:
#        if authenticator.update_user_details(st.session_state["username"]):
#            st.success('Entries updated successfully')
#    except Exception as e:
#        st.error(e)



#update config file
#This does not update a git hub page. Would need to have file in database and give streamlit access
#with open('multipage1/diagnose/config.yaml', 'w') as file:
#    yaml.dump(config, file, default_flow_style=False)

