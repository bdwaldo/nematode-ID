import streamlit as st
import csv
import pandas as pd

edit_df = pd.DataFrame(
  [
    {"Sample ID": ""},
    {"State sample collected": ""},
    {"Location identifier": ""},
    {"Sample Type": ""},
    {"Crop": ""},
    {"Variety": ""},
    {"Symptoms": ""}
  ]
)

with st.form("my_form"):
  st.write("Sample Information")
  submitter = st.text_input("Submitter name")
  phone = st.text_input("Submitter phone number")
  email = st.text_input("Submitter email address")
  date = st.date_input("Date sample collected", format="MM.DD.YYYY")
  st.data_editor(edit_df, num_rows = "dynamic")
  submitted = st.form_submit_button('Submit')

df = {'Sample submitter': [submitter],
      'Submitter Phone': [phone],
      'Email': [email],
      'Date collected': [date]
     }









#st.write(st.data_editor(edit_df, num_rows = "dynamic"))
         
#print input on screen
#st.write(df)



