import streamlit as st
import csv
import pandas as pd

#dictionary for editable portion of form
edit_df = pd.DataFrame(
  [
    {"Sample ID": ""},
    {"State sample collected": ""},
    {"Location identifier": ""},
    {"Sample type": ""},
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
  ed = st.data_editor(edit_df, num_rows = "dynamic")
  submitted = st.form_submit_button('Submit')

df = {'Sample submitter': [submitter],
      'Submitter Phone': [phone],
      'Email': [email],
      'Date collected': [date]
     }


#convert data into pandas data frame
df = pd.DataFrame(data=df)
df2 = pd.DataFrame(data=ed)
dd = df.concat(df2, ignore_index=True)

st.write(dd)
