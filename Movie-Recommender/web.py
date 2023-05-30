import streamlit as st
import pandas as pd
import pickle

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


movies_dict = pickle.load(open('moviedict.pickle','rb'))
df = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox('Select any movie',(df.title.values))
similarity = pickle.load(open('similarity.pickle','rb'))

st.text('click on recommend')


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



