#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

import streamlit as st

home = st.Page(
    "Home.py", title="Home", icon = ":material/home:", default=True)

id_now = st.Page("ID_Now.py", title="ID Now", icon=":material/arrow_forward:", default=False)

login = st.Page(
    "multipage1/diagnose/Login.py", title="Login", icon=":material/login:", default=False)

single = st.Page(
    "multipage1/diagnose/Single.py", title="Single", icon=":material/file_open:", default=False)

batch = st.Page(
    "multipage1/diagnose/Batch.py", title = "Batch", icon=":material/stacks:", default=False) 

tutorial = st.Page(
    "multipage1/help/Tutorial.py", title="Tutorial", icon=":material/text_snippet:",  default=False
)

faq = st.Page(
    "multipage1/help/FAQ.py", title="FAQ", icon=":material/help:", default=False
)

contact = st.Page(
    "multipage1/help/Contact.py", title="Contact", icon=":material/info:", default=False
)



pg = st.navigation(
  { "": [home],
    "ID Now": [id_now],
    "Diagnose Sample": [login, single, batch],
    "Help":[tutorial, faq, contact]
  }
)

pg.run()
