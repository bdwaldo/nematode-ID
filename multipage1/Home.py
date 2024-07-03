#Homepage
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 
  
st.set_page_config(page_title = "This is a Multipage WebApp") 
st.title("This is the Home Page.")

#create sidebar. Will have a background color green to indicate success
st.sidebar.success("Select Any Page from here") 

Diagnose = st.Page(
    "multipage1/Diagnose Samples/Diagnose Samples.py", title="Diagnose Samples", icon=":material/dashboard:", default=True
)
#st.Page("Diagnose Samples/Single.py", title="Single", icon=":material/bug_report:")

pg = st.navigation(
        {"Reports": [dashboard, bugs, alerts]})
