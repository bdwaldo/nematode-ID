#https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

import streamlit as st

st.set_page_config(
    page_title="Hello",
    #page_icon="👋",
)

st.write("# Welcome to Nematode ID!")

st.sidebar.success("Select a Page.")

st.markdown(
    """
    Nematode ID is a source for identifying plant-parasitic nematodes from images.
    **Select a page from the sidebar** to get started.
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io) #text to display in [] andlink in ()

    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
"""
)
