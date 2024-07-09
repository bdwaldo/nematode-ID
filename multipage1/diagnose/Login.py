#login page
#https://pypi.org/project/streamlit-authenticator/
  
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('./config/auth.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
st.write(config) # DEBUG 1

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)
authenticator.login()

if "authenticator" not in st.session_state:
    st.session_state["authenticator"] = authenticator

if st.session_state["authentication_status"] == False:
    st.error("Wrong username or password")
elif st.session_state["authentication_status"] == None:
    st.warning("Please insert your credentials")
elif st.session_state["authentication_status"]: 
    if "loggedIn" not in st.session_state:
        st.session_state["loggedIn"] = True

    try:
        if st.session_state["authenticator"].reset_password(st.session_state["username"]): 
            st.success('Password modified successfully')      
    except Exception as e:    
        st.error(e)
    st.write(config) # DEBUG 2
    st.write(st.session_state) # DEBUG 3
    with open('./config/auth.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
