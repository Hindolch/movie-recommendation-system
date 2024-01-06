import streamlit as st
import pickle
import numpy as np


df = pickle.load(open('df.pkl', 'rb'))
indipkl = pickle.load(open('Indices.pkl', 'rb'))
similarity_score = pickle.load(open('similarityScore.pkl', 'rb'))
drama_movies = pickle.load(open('dramaMovies.pkl', 'rb'))
comedy_movies = pickle.load(open('comedyMovies.pkl', 'rb'))
action_movies = pickle.load(open('actionMovies.pkl', 'rb'))
romance_movies = pickle.load(open('romMovies.pkl', 'rb'))
crime_movies = pickle.load(open('crimeMovies.pkl', 'rb'))
horror_movies = pickle.load(open('horrorMovies.pkl', 'rb'))
anim_movies = pickle.load(open('animMovies.pkl', 'rb'))
scifi_movies = pickle.load(open('scifiMovies.pkl', 'rb'))
mystery_movies = pickle.load(open('mysteryMovies.pkl', 'rb'))


st.title('Movie recommendation system')
def recommend(title, indices=indipkl, cosine_sim = similarity_score, num_recommendation=5):
    title = title.replace(' ', '').lower()
    x = []
    try:
        idx = indipkl[title]
        sim_score = cosine_sim[idx]
        ranked_indices = np.argsort(sim_score)[::-1]
        close_indices = ranked_indices[1: num_recommendation + 1]
        close_movies = [(df.iloc[i]['Title']) for i in close_indices]
        x.append(close_movies)
        st.write('Here are the top 5 recommendations')
        for i in x:
            return i
        x.clear()
    except:
        st.write('Sorry :(  We do not have this movie in the dataset')

query = st.text_input('Enter any movie you like and we will recommend more movies like this')
if st.button('Recommend'):
    rec = recommend(query)
    st.write(rec)


def drama():
    st.write('Here are the top recommendations')
    for a,b in drama_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)

def comedy():
    st.write('Here are the top recommendations')
    for a,b in comedy_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)

def action():
    st.write('Here are the top recommendations')
    for a,b in action_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)


def romance():
    st.write('Here are the top recommendations')
    for a,b in romance_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)

def crime():
    st.write('Here are the top recommendations')
    for a,b in crime_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)

def horror():
    st.write('Here are the top recommendations')
    for a,b in horror_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)


def animation():
    st.write('Here are the top recommendations')
    for a,b in anim_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)

def scifi():
    st.write('Here are the top recommendations')
    for a,b in scifi_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)


def mystery():
    st.write('Here are the top recommendations')
    for a,b in mystery_movies.items():
        st.write('Name:', a)
        genre = b['Genre']
        imdb_score = b['IMDb Score']
        st.write('Genre:', genre)
        st.write('IMDb Score:', imdb_score)



query2 = st.text_input('Enter any genre you like and we will recommend the best movies in it').lower()
if st.button('Recommend this genre shows'):
    if query2 == 'drama':
        drama()
    elif query2 == 'comedy':
        comedy()
    elif query2 == 'action':
        action()
    elif query2 == 'romance':
        romance()
    elif query2 == 'crime':
        crime()
    elif query2 == 'horror':
        horror()
    elif query2 == 'animation':
        animation()
    elif query2 == 'scifi' or query2 == 'sci-fi':
        scifi()
    else:
        mystery()
