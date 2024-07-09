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
df3 = pd.concat([df, df2])


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


##########################################
#positioning buttons in columns

col1, col2 = st.columns(2)

#See summary of sample info
with col1:
  if st.button('Summary'):
    st.write(df3)


#################################################
#convert data frame to csv and download
#https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv
with col2:
  @st.cache_data #iportant so doesn't rerun each time
  def convert_df(df3):
    return df3.to_csv(index=False).encode('utf-8')
 csv_file = convert_df(df)
 st.download_button(
   label = "Download CSV",
   data = csv_file,
   file_name = (f"{name}.csv"),
   mime = "text/csv",
   key='download-csv'
)



  







