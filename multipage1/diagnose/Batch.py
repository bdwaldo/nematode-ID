import streamlit as st
import csv
import pandas as pd


with st.form("my_form"):
  st.write("Sample Information")
  submitter = st.text_input("Submitter name")
  phone = st.text_input("Submitter phone number")
  email = st.text_input("Submitter email address")
  date = st.date_input("Date sample collected", format="MM.DD.YYYY")

edit_df = pd.DataFrame(
  [
    {"Sample ID": ""},
    {"State sample collected": ""},
    {"Location identifier": "", "", "", "", "", "", "", "", "", ""},
    sample_type = {"Sample Type": "", "", "", "", "", "", "", "", "", ""},
    crop = {"Crop": "", "", "", "", "", "", "", "", "", ""},
    variety = {"Variety": "", "", "", "", "", "", "", "", "", ""},
    symptoms = {"Symptoms": "", "", "", "", "", "", "", "", "", ""}
  ]
)


#fields = [sample_submitter, sample_id, phone, 
#          email, date, state, location,
#          sample_type, crop, variety, symptoms]

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
df = pd.DataFrame(data=df)

st.write(st.data_editor(edit_df, num_rows = "dynamic"))
#print input on screen
#st.write(df)



