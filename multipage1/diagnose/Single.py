import streamlit as st

form = st.form("my_form")
st.write("Sample Information")
st.text_input("Sample ID")

# Now add a submit button to the form:
form.form_submit_button("Submit")
