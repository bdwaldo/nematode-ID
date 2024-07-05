#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

import streamlit as st

home = st.Page(
    "Home.py", title="Home", icon=":material/dashboard:", default=True
)
id_now = st.Page("ID Now.py", title="ID Now", icon=":material/bug_report:",default=True)
single = st.Page(
    "diagnose/Single.py", title="Diagnose Samples", icon=":material/notification_important:", default=True
)
batch = st.Page(
    "diagnose/Batch.py", title = "Batch", default=True) 

tutorial = st.Page(
    "help/Tutorial.py", title="Tutorial", icon=":material/dashboard:", default=True
)

help = st.Page(
    "help/Help.py", title="Tutorial", icon=":material/dashboard:", default=True
)



pg = st.navigation(
  {
    "Home": [home],
    "ID Now": [id_now],
    "Diagnose": [single, batch],
    "Help":[tutorial, help]
  }
)

pg.run()
