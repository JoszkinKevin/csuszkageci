import streamlit as st

st.title("csuszka")
level = st.slider(".slider: Select the level", 1, 5)

st.text('Selected: {}'.format(level))
