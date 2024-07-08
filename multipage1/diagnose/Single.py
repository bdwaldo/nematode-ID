import streamlit as st


with st.form("my_form"):
  st.write("Sample Information")
  sample_id = st.text_input("Sample ID")
  sample_collected = st.text_input("State sample collected")
  location = st.text_input("Location identifier (field, green...etc)") 
  sample_type = st.selectbox('Sample Type', ["","soil", "roots", "leaves"])
  crop = st.text_input("Crop")
  variety = st.text_input("Variety")
  symptoms = st.selectbox('Symptoms', ["","none", "galling", "stunted roots", "wilting", "chlorosis", "other"])
  submitted = st.form_submit_button('Submit')

d = {‘Book Name(s)’: [newBookName],
‘Book Author(s)’: [newBookAuthor],
‘Feedback’: [newFeedback],
‘Name’: [emailName],
‘Email’: [emailAddress]}
df = pd.DataFrame(data=d)
