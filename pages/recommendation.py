import streamlit as st
from utils import recommend
import pickle

movies = pickle.load(open("movies.pickle","rb"))

movie_list = movies["title"].values

st.title("Movie Recommendation")

selected_movie = st.selectbox(
    "Select Movie",
    movie_list
)

if st.button("Recommend Movies"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.write("Poster not available")

            st.write(name)