import streamlit as st


with st.form("my_form"):
  st.write("Sample Information")
  sample_submitter = st.text_input("Sample submitter")
  phone = st.text_input("Submitter phone number")
  email = st.text_input("Submitter email address")
  sample_id = st.text_input("Sample ID")
  date = st.date_input("Date sample collected")
  state = st.text_input("State sample collected")
  location = st.text_input("Location identifier (field, green...etc)") 
  sample_type = st.selectbox('Sample Type', ["","soil", "roots", "leaves"])
  crop = st.text_input("Crop")
  variety = st.text_input("Variety")
  symptoms = st.selectbox('Symptoms', ["","none", "galling", "stunted roots", "wilting", "chlorosis", "other"])
  submitted = st.form_submit_button('Submit')

df = {'Sample submitter': [sample_submitter],
      'Sample ID': [sample_id],
      'Submitter Phone': [phone],
      'Email': [email]
      'Date collected': [date],
      'State Sample Collected': [state],
      'Location': [location],
      'Sample Type': [sample_type],
      'Crop': [crop],
      'Variety': [variety],
      'Symptoms': [symptoms],
           }
df = df.append(pd.DataFrame(data=df))
print(df)
