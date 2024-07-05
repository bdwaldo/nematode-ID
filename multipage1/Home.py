#https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

import streamlit as st

#st.set_page_config(
#    page_title="Welcome")
   

st.write("# Welcome to Nematode ID!")

st.sidebar.success("Select a Page.")

st.markdown(
    """
    Nematode ID is a source for identifying plant-parasitic nematodes from images.
    **Select a page from the sidebar** to get started.
    ### Want to learn more?
    - Check out the [Tutorial](https://streamlit.io)

    ### Basic Information
    - See the [Help](https://github.com/streamlit/demo-self-driving) page
"""
)
