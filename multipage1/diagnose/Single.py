import streamlit as st


with st.form("my_form"):
  st.write("Sample Information")
  st.text_input("Sample ID")
  st.text_input("State sample collected")
  st.text_input("Location identifier (field, green...etc)") 
  st.selectbox('Sample Type', ["","soil", "roots", "leaves"])
  st.text_input("Crop")
  st.text_input("Variety")
  st.selectbox('Symptoms', ["","none", "galling", "stunted roots", "wilting", "chlorosis", "other"])
  submitted = st.form_submit_button('Submit')


