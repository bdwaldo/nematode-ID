#https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

home = st.Page(
    "multipage1/home.py", title="Home", icon=":material/dashboard:", default=True
)
id_Now = st.Page("multipage1/ID Now.py", title="ID Now", icon=":material/bug_report:")
diagnose = st.Page(
    "diagnose/Diagnose Samples.py", title="Diagnose Samples", icon=":material/notification_important:"
)

tutorial = st.Page(
    "multipage1/help/Tutorial.py", title="Tutorial", icon=":material/dashboard:", default=True
)

help = st.Page(
    "multipage1/help/Help.py", title="Tutorial", icon=":material/dashboard:", default=True
)



pg = st.navigation(
  {
    "Home": [home],
    "ID Now": [id_now],
    "Diagnose": [search, history],
    "Help":[tutorial, help]
  }
)

pg.run()
