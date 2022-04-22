import pickle
import numpy as np
import streamlit as st
from itertools import chain
from sklearn.neighbors import NearestNeighbors
#import requests



def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = cluster.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors =6)
    suggestions = list(chain.from_iterable(suggestions))
    recommended_books_names = []
    recommended_books_posters = []
    suggestions = suggestions[1:]
    for i in range(len(suggestions)):
        #print(book_pivot.index[suggestions[i]])
        #movie_id = movies.iloc[i[0]].movie_id
        recommended_books_names.append(book_pivot.index[suggestions[i]])

        recommended_books_posters.append(movies["Image-URL-L"].iloc[suggestions[i]])


    return recommended_books_names,recommended_books_posters

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#
#     return recommended_movie_names,recommended_movie_posters


st.header('Books You Would Like')
movies = pickle.load(open('final_rating.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))
cluster= pickle.load(open('cluster.pkl','rb'))
# similarity = pickle.load(open('model/similarity.pkl','rb'))
#
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a book from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend_book(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
