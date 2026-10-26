import streamlit as st
import pickle
from utils import fetch_poster

# Load movies
movies = pickle.load(open("movies.pickle", "rb"))

st.title("Movie Search")

# Search box
movie = st.text_input("Search for a movie")

if movie:

    filtered_movies = movies[
        movies["title"].str.contains(movie, case=False, na=False)
    ]

    if filtered_movies.empty:
        st.warning("No movies found.")

    else:
        for _, row in filtered_movies.iterrows():

            col1, col2 = st.columns([1, 3])

            with col1:
                poster = fetch_poster(row["movie_id"])

                if poster:
                    st.image(poster, width=120)

            with col2:
                st.subheader(row["title"])
                st.write(f"⭐ Rating: {row['vote_average']}")
                st.write(f"📅 Release Date: {row['release_date']}")
                st.write(row["overview"][:200] + "...")
                st.divider()