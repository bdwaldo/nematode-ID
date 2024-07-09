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




#convert data into pandas data frame
#df = pd.DataFrame(data=df)

st.write(st.data_editor(edit_df, num_rows = "dynamic"))
#print input on screen
#st.write(df)



