import streamlit as st
import pickle
import pandas as pd
import requests

# Load saved data
movies = pickle.load(open('data.pkl', 'rb'))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)


# TMDb API Key
TMDB_API_KEY = 'c65da46f51f1bacedb6f3ab8fe9e4f9f'

# App Title
st.title("🎬 Movie Recommendation System")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie:", movies['primaryTitle'].values)

# Dropdown for genre selection
all_genres = sorted(list(set(g for genre_list in movies['genres'].dropna().str.split(',') for g in genre_list)))
selected_genre = st.selectbox("Or select a genre:", all_genres)

# Fetch poster using TMDb
def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
    return None

# Movie-based recommendation
def recommend(movie):
    movie = movie.lower()
    matches = movies[movies['primaryTitle'].str.lower() == movie]

    if matches.empty:
        return []

    index = matches.index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:21]

    recommendations = []
    for i in movie_list:
        title = movies.iloc[i[0]].primaryTitle
        rating = movies.iloc[i[0]].averageRating if 'averageRating' in movies.columns else 0
        recommendations.append((title, rating))
    
    return sorted(recommendations, key=lambda x: x[1], reverse=True)[:5]

# Genre-based recommendation
def recommend_by_genre(genre):
    filtered = movies[movies['genres'].str.contains(genre, case=False, na=False)]
    top_movies = filtered.sort_values(by='averageRating', ascending=False).head(5)
    return list(zip(top_movies['primaryTitle'], top_movies['averageRating']))

# Show movie recommendations
if st.button("🎥 Recommend by Movie"):
    results = recommend(selected_movie)
    if results:
        st.subheader("You might also like:")
        for title, rating in results:
            poster_url = fetch_poster(title)
            col1, col2 = st.columns([1, 4])
            with col1:
                if poster_url:
                    st.image(poster_url, width=100)
                else:
                    st.text("No Poster")
            with col2:
                st.markdown(f"**{title}** (⭐ {rating})")
    else:
        st.warning("❌ Movie not found or no recommendations available.")

# Show genre-based recommendations
if st.button("🎞️ Recommend by Genre"):
    genre_results = recommend_by_genre(selected_genre)
    if genre_results:
        st.subheader(f"Top Rated Movies in '{selected_genre}' Genre:")
        for title, rating in genre_results:
            poster_url = fetch_poster(title)
            col1, col2 = st.columns([1, 4])
            with col1:
                if poster_url:
                    st.image(poster_url, width=100)
                else:
                    st.text("No Poster")
            with col2:
                st.markdown(f"**{title}** (⭐ {rating})")
    else:
        st.warning("❌ No movies found for this genre.")
