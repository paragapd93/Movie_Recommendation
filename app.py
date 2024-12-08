import streamlit as st
import traceback
import pickle
import pandas as pd

#create the recommendation
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[0:5]

    recommended_list = []
    for i in movies_list:
        recommended_list.append(movies.iloc[i[0]].title)

    return recommended_list

try:
    movies_dict = pickle.load(open(r'D:\ML_2024\ML_2024\Movie Recommendation\movie_dict.pkl','rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open(r'D:\ML_2024\ML_2024\Movie Recommendation\similarity.pkl', 'rb'))

    st.title("Movie Recommender System")
    selected_movie = st.selectbox('How would you line to be contacted?',movies['title'].values)

    if st.button('Recommend'):
        recommended_list = recommend(selected_movie)
        for i in recommended_list:
            st.write(i)

except Exception as e:
    print(traceback.format_exc())