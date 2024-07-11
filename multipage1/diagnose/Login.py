import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Load your configuration file (replace '../config.yaml' with your actual path)
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

# Hash passwords (this will automatically hash plain text passwords in the config)
hashed_passwords = authenticator.hash_passwords()

# Now replace plain text passwords in the configuration file with the hashed passwords
# (you don't need to manually hash them)
# ...

# Use the hashed passwords as needed
# ...


