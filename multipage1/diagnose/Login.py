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
if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')


#update user information
usernames = config['cookie']['name']


with st.form("edit_profile"):
  st.write("Edit Profile")
  new_name = st.text_input("New name")
  submitted = st.form_submit_button('Submit Form')
  if (config['cookie']['name'] == new_name):
      st.warning('Name already in use.')
  else:
      config['cookie']['name'] = new_name




#update config file
with open('multipage1/diagnose/config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
