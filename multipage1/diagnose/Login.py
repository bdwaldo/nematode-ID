import streamlit as st
import os

st.header("Login to account")
st.markdown('''This is a demo for a login page. I envision using accounts to store and track
sample information for diagnostics.''')

st.caption('''I have created accounts manually for this example. 
I would need to connect the signup page to a database in order to 
securely store and update user information.''') 

usernames = st.secrets.un
passwords = st.secrets.pw

def sign_in():
  with st.form(key='login', clear_on_submit = True): 
    st.subheader('Login')
    username = st.text_input('Username', placeholder='Enter your username')
    password = st.text_input('Password', placeholder='Enter your password')
    st.form_submit_button('Login')  

    #check that username and password in list match
    for i in range(len(usernames)):
      if username == usernames[i] and password == passwords[i]:
        st.write("Login successful")
        break
    else: 
      st.warning("Username/password invalid")
      
      
sign_in()


#print username list (un)
for x in range(len(st.secrets.un)):
  st.write(st.secrets.un[x])

st.write(st.secrets.bw["username"])
st.write(st.secrets.bw["name"])


