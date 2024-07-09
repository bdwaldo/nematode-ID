import streamlit as st
import csv
import pandas as pd


with st.form("my_form"):
  st.write("Sample Information")
  submitter = st.text_input("Submitter name")
  phone = st.text_input("Submitter phone number")
  email = st.text_input("Submitter email address")
  date = st.date_input("Date sample collected", format="MM.DD.YYYY")
  submitted = st.form_submit_button('Submit')




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


df = {'Sample submitter': [submitter],
      'Sample ID': [sample_id],
      'Submitter Phone': [phone],
      'Email': [email],
      'Date collected': [date],
      'State Sample Collected': [state],
      'Location': [location],
      'Sample Type': [sample_type],
      'Crop': [crop],
      'Variety': [variety],
      'Symptoms': [symptoms],
           }

#convert data into pandas data frame
#df = pd.DataFrame(data=df)

st.write(st.data_editor(edit_df, num_rows = "dynamic"))
#print input on screen
#st.write(df)



