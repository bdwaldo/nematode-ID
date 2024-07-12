#streamlit authenticator login
#https://github.com/mkhorasani/Streamlit-Authenticator/tree/main?tab=readme-ov-file#authenticatelogin

import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Load your configuration file (replace '../config.yaml' with your actual path)
#make sure yaml file extension is correct. won't work if created in jupytr notebook
with open('multipage1/diagnose/config.yaml') as file:
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


#reset password
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)


#New user
try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
    if email_of_registered_user:
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

#forgot password
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # The developer should securely transfer the new password to the user.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)


#forgot username
try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username to be sent securely')
        # The developer should securely transfer the username to the user.
    elif username_of_forgotten_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)
    

#####################
#update user information
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

st.write(config.jsmith['name'])


#update user information
#usernames = config['credentials']['usernames']
#st.write = usernames


#Trying to acutally update name
#with st.form('edit_profile'):
#    st.write('Edit Name')
#    new_name = st.text_input('New name')
#    submitted = st.form_submit_button('Submit Form')
#    if (config['cookie']['name'] == new_name):
#        st.warning('Name already in use.')
#    else:
#        config['cookie']['name'] = new_name


#update config file
with open('multipage1/diagnose/config.yaml', 'w') as file:
    yaml.safe_dump(config, file, default_flow_style=False)
file.close()
