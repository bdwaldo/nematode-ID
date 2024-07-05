import streamlit as st

form = st.form("my_form")
st.write("Sample Information")
st.text_input("Sample ID")
st.text_input("State sample collected")
st.text_input("Location identifier (field, green...etc) 
st.selectbox('Sample Type', ["","soil", "roots", "leaves"])
st.text_input("crop")
st.text_input("variety")
st.selectbox('Symptoms', ["","none", "galling", "stunted roots", "wilting", "chlorosis", "other"])



# Now add a submit button to the form:
form.form_submit_button("Submit")
