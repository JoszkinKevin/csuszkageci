import streamlit as st

st.title("csuszka")
szint = st.slider("valasszal szamot csoves", 0, 16)


st.text('valasztott: {}'.format(2**szint))
