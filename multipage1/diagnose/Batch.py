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



