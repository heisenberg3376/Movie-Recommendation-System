import streamlit as st
import pandas as pd
import pickle
import _pickle as cPickle
import bz2
import requests

def recommend(movie):
    movie_index = df[df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    movies_id = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_posters

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d7a02be257792ab6e3aaa6698cf9c241&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

    
st.title('Movie Recommendation System')


def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data


movies_dict = pickle.load(open('moviedict.pickle','rb'))
df = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox('Select any movie',(df.title.values))
similarity = decompress_pickle('similarity1.pbz2')

st.text('click on recommend')


if st.button('Recommend'):
    recommendations,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])



