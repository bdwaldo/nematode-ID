#Homepage
#https://www.geeksforgeeks.org/creating-multipage-applications-using-streamlit/

import streamlit as st 
  
#st.set_page_config(page_title = "This is a Multipage WebApp") 
#st.title("This is the Home Page.")

#create sidebar. Will have a background color green to indicate success
#st.sidebar.success("Select Any Page from here") 


#########################
#pg = st.navigation([st.Page("pages/ID Now.py"), st.Page("pages/Nematode Profiles.py")])
#pg.run()


##########################
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "pages/Diagnose Samples/Single.py", title="Single", icon=":material/dashboard:", default=True
)
#bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
#alerts = st.Page(
#    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
#)

#search = st.Page("tools/search.py", title="Search", icon=":material/search:")
#history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            #"Account": [logout_page],
            "Reports": [dashboard]#, bugs, alerts],
            #"Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
