import pickle
import streamlit as st
import requests


# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bb47c28a56852aa1d4564ef8fddc7bc3&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get("poster_path", "")
    full_path = f"http://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
    return full_path


# Function to recommend movies
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1],
    )
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name, recommended_movies_poster


# Load movie data and similarity matrix
movies = pickle.load(open("artifacts/movie_list.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))

# Set up page layout
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown(
    """
    <style>
    .main-header {
        background-image: url('https://source.unsplash.com/1600x900/?movies,cinema');
        background-size: cover;
        padding: 2rem;
        color: white;
        text-align: center;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header section
st.markdown(
    """
    <div class="main-header">
        <h1>🎥 Movie Recommender System</h1>
        <p>Discover your next favorite movie with personalized recommendations!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Movie selection
st.subheader("Select a Movie 🎬")
movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie", movie_list)

# Show recommendations
if st.button("🎉 Show Recommendations"):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)

    st.subheader(f"Movies similar to **{selected_movie}**:")

    # Create 5 columns for displaying the recommendations horizontally
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Display recommended movies in columns
    with col1:
        st.image(recommended_movies_poster[0], width=200)
        st.markdown(f"<h4 style='text-align: center;'>{recommended_movies_name[0]}</h4>", unsafe_allow_html=True)
    with col2:
        st.image(recommended_movies_poster[1], width=200)
        st.markdown(f"<h4 style='text-align: center;'>{recommended_movies_name[1]}</h4>", unsafe_allow_html=True)
    with col3:
        st.image(recommended_movies_poster[2], width=200)
        st.markdown(f"<h4 style='text-align: center;'>{recommended_movies_name[2]}</h4>", unsafe_allow_html=True)
    with col4:
        st.image(recommended_movies_poster[3], width=200)
        st.markdown(f"<h4 style='text-align: center;'>{recommended_movies_name[3]}</h4>", unsafe_allow_html=True)
    with col5:
        st.image(recommended_movies_poster[4], width=200)
        st.markdown(f"<h4 style='text-align: center;'>{recommended_movies_name[4]}</h4>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Built with ❤️ using Streamlit | Data sourced from TMDb API</p>
        <p>🔗 <a href="https://www.themoviedb.org/">The Movie Database</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
