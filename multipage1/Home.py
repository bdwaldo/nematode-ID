#Homepage
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 
  
st.set_page_config(page_title = "This is a Multipage WebApp") 
st.title("This is the Home Page.")

#create sidebar. Will have a background color green to indicate success
st.sidebar.success("Select Any Page from here") 

Single = st.Page(
    "multipage1/Diagnose Samples/Single.py", title="Diagnose Samples", icon=":material/dashboard:", default=True
)
#st.Page("Diagnose Samples/Single.py", title="Single", icon=":material/bug_report:")

pg = st.navigation(
        {"Reports": [Single]})
