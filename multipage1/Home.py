#Homepage
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 

st.set_page_config(page_title = "Nematode ID") 
st.title("Nematode ID")

#create sidebar. Will have a background color green to indicate success
st.sidebar.success("Select Any Page from here") 
 


#########################
#pg = st.navigation([st.Page("pages/ID Now.py"), st.Page("pages/Nematode Profiles.py")])
#pg.run()

#####################
diagnose = st.Page(
    "Diagnose/Diagnose Samples.py", title="Diagnose", icon=":material/dashboard:", default=True
)
single = st.Page("Diagnose/Single.py", title="Single", icon=":material/bug_report:")
batch = st.Page(
    "Diagnose/Batch.py", title="Batch", icon=":material/notification_important:"
)
id_now = st.Page("pages/ID now.py", title = "ID Now", default = True)

pg = st.navigation(
        {
            "Diagnose": [logout_page],
            "Diagnose": [dashboard, bugs, alerts],
            "ID now": [id_now]
        }
    )

pg.run()


