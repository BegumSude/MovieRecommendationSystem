from kaggle.api.kaggle_api_extended import KaggleApi
from PIL import Image
from io import BytesIO
import streamlit as st
import pandas as pd
import json
import requests
import time
import os

api = KaggleApi()
api.authenticate()

movies = pd.read_csv('//Users/begumsudebolukbas/Desktop/MovieRecommendationSystem/tmdb_10_movies.csv')
tmdb_api_key = '6c735c81a272ff62c18e6a22aefdc12e'

movies_titles = movies['title'].tolist()

posters_urls = []

for title in movies_titles:
    base_url = "https://api.themoviedb.org/3/search/movie"
    parameters = {
        "api_key": tmdb_api_key,
        "query": title,
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                full_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
                posters_urls.append((title, full_url))
            else:
                posters_urls.append((title, None))
        else:
            posters_urls.append((title, None))
    else:
        posters_urls.append((title, None))
    time.sleep(0.1)

os.makedirs("Posters", exist_ok=True)

for title, url in posters_urls:
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(f"Posters/{title}.jpg")

poster_df = pd.DataFrame(posters_urls, columns=["title", "poster_url"])
poster_df.to_csv("movie_posters.csv", index=False)

movies = pd.merge(movies, poster_df, on="title", how="left")

genres = ["Action", "Adventure", "Fantasy", "Science Fiction", "Crime","Thriller","Drama",
          "Animation", "Family", "Comedy", "Western", "Romance", "Horror", "History"]

keywords = ["animation", "superhero", "revenge", "escape", "batman",
            "terrorist", "spy", "united kingdom", "ocean", "ship",
            "pirate", "soldier", "future", "flood", "princess",
            "marvel comic","magic", "musical", "tower", "blond woman",
            "culture clash", "dc comics", "mars", "hostage", "witch",
            "sea", "shipwreck", "artificial intelligence", "spacecraft"]

st.title(' Movie Recommendation System ')
st.title("🎬🍿🎥🎬🍿🎥🎬🍿🎥🎬🍿🎥🎬🍿")

genre = st.selectbox('Select a movie genre', genres)
keyword = st.selectbox('Select a keyword to search for movies', keywords)

def get_genres_from_json(json_str):
    try:
        genres = json.loads(json_str)
        genre_names = [genre['name'] for genre in genres]
        return genre_names
    except:
        return []

def get_keywords_from_json(json_str):
    try:
        keywords = json.loads(json_str)
        keyword_names = [keyword['name'] for keyword in keywords]
        return keyword_names
    except:
        return []

if st.button("Recommend 🕵🏻‍‍️"):
    if genre and keyword:
        filtered_movies = movies[
            movies['genres'].apply(lambda x: genre in get_genres_from_json(x) if isinstance(x, str) else False) &
            movies['keywords'].apply(lambda x: keyword in get_keywords_from_json(x) if isinstance(x, str) else False)
            ]

    if filtered_movies.empty:
        st.write(f"No movies found for the genre: '{genre}' and keyword: '{keyword}'.")
    else:
        st.write(f"Found {len(filtered_movies)} movies for the genre: '{genre}' and keyword '{keyword}':")
        for index, row in filtered_movies.iterrows():
            col1, col2 = st.columns([1, 2])

            with col1:
                if isinstance(row['poster_url'], str) and row['poster_url'].startswith("http"):
                    st.image(row['poster_url'], caption=row['title'], width=200)

                else:
                    st.write("Poster is not available.")

            with col2:
                st.subheader(row['title'])
                st.write(f"Overview: {row['overview']}")
                st.write(f"Average Vote: {row['vote_average']}")
                st.write(f"Duration of the movie: {row['runtime']} minutes")

                if row['homepage']:
                    st.markdown(f"[Go to {row['title']} Homepage]({row['homepage']})", unsafe_allow_html=True)

            st.markdown("---")






