#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

import streamlit as st

home = st.Page(
    "Home.py", title="Home", icon = ":material/home:", position = hidden, default=True
)
id_now = st.Page("ID Now.py", title="ID Now", icon=":material/arrow_forward:", default=False)

single = st.Page(
    "diagnose/Single.py", title="Single", icon=":material/file_open:", default=False
)
batch = st.Page(
    "diagnose/Batch.py", title = "Batch", icon=":material/stacks:", default=False) 

tutorial = st.Page(
    "help/Tutorial.py", title="Tutorial", icon=":material/text_snippet:",  default=False
)

faq = st.Page(
    "help/FAQ.py", title="FAQ", icon=":material/help:", default=False
)

contact = st.Page(
    "help/Contact.py", title="Contact", icon=":material/info:", default=False
)



pg = st.navigation(
  { "Home": [home],
    "ID Now": [],
    "Diagnose Sample": [single, batch],
    "Help":[tutorial, faq, contact]
  }
)

pg.run()
