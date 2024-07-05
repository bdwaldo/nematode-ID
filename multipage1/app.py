#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

import streamlit as st

home = st.Page(
    "Home.py", title="Home", icon=":material/dashboard:", default=True
)
id_now = st.Page("ID Now.py", title="ID Now", icon=":material/bug_report:",default=False)
single = st.Page(
    "diagnose/Single.py", title="Diagnose Samples", icon=":material/notification_important:", default=False
)
batch = st.Page(
    "diagnose/Batch.py", title = "Batch", default=False) 

tutorial = st.Page(
    "help/Tutorial.py", title="Tutorial", icon=":material/dashboard:", default=False
)

faq = st.Page(
    "help/Help.py", title="FAQ", icon=":material/dashboard:", default=False
)

support = st.Page(
    "help/Support.py", title="FAQ", icon=":material/dashboard:", default=False
)



pg = st.navigation(
  {
    "Home": [],
    "ID Now": [],
    "Diagnose": [single, batch],
    "Help":[tutorial, faq, support]
  }
)

pg.run()
