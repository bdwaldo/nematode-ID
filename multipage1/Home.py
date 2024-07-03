#Homepage
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 
  
st.set_page_config(page_title = "This is a Multipage WebApp") 
st.title("This is the Home Page.")

#create sidebar. Will have a background color green to indicate success
st.sidebar.success("Select Any Page from here") 

#create a directory in the same location as this file with the name, "pages".
#The page names will showup in the didebar of this home page
#pages are listed alphabetically by defalt
