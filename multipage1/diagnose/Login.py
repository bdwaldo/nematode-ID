import streamlit as st
import os



#print username list (un)
for x in range(len(st.secrets.un)):
  st.write(st.secrets.un[x])

st.write(st.secrets.b["username"])
st.write(st.secrets.b["name"])


