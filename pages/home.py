import streamlit as st

st.title("Home")

col1,col2=st.columns([2,1])

with col1:

    st.markdown("""
    ## Welcome

    This project recommends movies using Content Based Filtering.

    Features

    - Smart Recommendations
    - Movie Search
    - Similar Movies
    - Fast Prediction
    - TMDB Dataset
    """)


st.divider()

c1,c2,c3=st.columns(3)

c1.metric("Movies","4803")

c2.metric("Algorithm","Content Based")

c3.metric("Language","Python")