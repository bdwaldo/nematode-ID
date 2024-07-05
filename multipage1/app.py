#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

import streamlit as st

home = st.Page(
    "Home.py", title="Home", default=True
)
id_now = st.Page("ID Now.py", title="ID Now", default=False)

single = st.Page(
    "diagnose/Single.py", title="Single", default=False
)
batch = st.Page(
    "diagnose/Batch.py", title = "Batch", default=False) 

tutorial = st.Page(
    "help/Tutorial.py", title="Tutorial",  default=False
)

faq = st.Page(
    "help/FAQ.py", title="FAQ", default=False
)

support = st.Page(
    "help/Support.py", title="Support", default=False
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
