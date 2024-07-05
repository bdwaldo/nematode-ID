
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 




home = st.Page(
 "multipage1/Home.py", title = "Home", default = True)

diagnose = st.Page(
    "Diagnose Samples/Diagnose Samples.py", title="Diagnose", icon=":material/dashboard:", default=True
)
single = st.Page("Diagnose Samples/Single.py", title="Single", icon=":material/bug_report:")
batch = st.Page(
    "Diagnose/Batch.py", title="Batch", icon=":material/notification_important:"
)
id_now = st.Page("pages/ID now.py", title = "ID Now", default = True)

pg = st.navigation(
        {
            "Home": [home],
            "Diagnose": [single, batch],
            "ID now": [id_now]
        }
    )

pg.run()


