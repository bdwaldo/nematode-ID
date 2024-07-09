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
  st.data_editor(edit_df, num_rows = "dynamic")
  submitted = st.form_submit_button('Submit')

df = {'Sample submitter': [submitter],
      'Submitter Phone': [phone],
      'Email': [email],
      'Date collected': [date]
     }


##############################
#AI generated code
# Initialize a list to store form submissions
@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

pageviews = Pageviews()

# Append a dummy value to the list when the form is submitted
pageviews.append('dummy')

# Now the length of the list represents the number of form submissions
number_of_submissions = len(pageviews)

#st.write(f"Number of form submissions: {number_of_submissions}")

#set f string to assign sample name
name = (f"Nematode-ID: NI{number_of_submissions}_{date}_{submitter}")
st.write(name)



