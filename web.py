import streamlit as st
import pandas as pd
import pickle
import _pickle as cPickle
import bz2

def recommend(movie):
    movie_index = df[df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    movies_id = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(df.iloc[i[0]].title)
        
    return recommended_movies

st.title('Movie Recommendation System')
st.write('''## select a movie and I will recommend 5 movies which are similar to it''')

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
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



