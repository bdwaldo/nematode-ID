import streamlit as st
import csv
import pandas as pd


with st.form("my_form"):
  st.write("Sample Submission Information")
  submitter = st.text_input("Submitter name")
  phone = st.text_input("Submitter phone number")
  email = st.text_input("Submitter email address")
  date = st.date_input("Date sample collected", format="MM.DD.YYYY")
  sample_id = st.text_input("Sample ID")
  state = st.text_input("State sample collected")
  location = st.text_input("Location identifier (field, green...etc)") 
  sample_type = st.selectbox('Sample Type', ["","soil", "roots", "leaves"])
  crop = st.text_input("Crop")
  variety = st.text_input("Variety")
  symptoms = st.selectbox('Symptoms', ["","none", "galling", "stunted roots", "wilting", "chlorosis", "other"])
  submitted = st.form_submit_button('Submit')

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

#print input on screen
#st.write(df)


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
name = (f"Nematode-ID: NI{number_of_submissions}_{date}_{submitter}_{sample_id}")
st.write(name)


#################################################
#convert data frame to csv and download
#https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv
@st.cache_data #iportant so doesn't rerun each time
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv_file = convert_df(df)

st.download_button(
   label = "Press to Download",
   data = csv_file,
   file_name = (f"{name}.csv"),
   mime = "text/csv",
   key='download-csv'
)


