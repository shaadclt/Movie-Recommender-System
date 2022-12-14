import streamlit as st
import pickle
import requests
from recommended_details import title, image, overview, release, keywords, genres
import lzma

st.set_page_config(page_title="Movie Recommender System", page_icon=None, layout="wide",
                   initial_sidebar_state="expanded", menu_items={"Get help": None, "Report a Bug": None, "About": None})

movie_list = pickle.load(lzma.open('movies.pickle', 'rb'))
similarity = pickle.load(lzma.open('similarity.pickle', 'rb'))

api_key = "328663c183ab4dee463d1288e55a00ae&language=en-US"

hide_menu_style = """
    <style>
        #MainMenu {visibility:hidden; }
        footer {visibility:hidden; }
        .css-b7s55g {width:37rem;} 
        button.css-1rs6os::before {content: "View your movie details here";}
        .css-hxt7ib h3 {font-size:0.925rem;}
        .css-1wrcr25 {overflow:auto;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)


def poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    poster_link = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return poster_link


def recommend(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movies_rec = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    movie_posters = []
    recommended = []
    for i in movies_rec:
        recommended.append(movie_list.iloc[i[0]].title)
        movie_posters.append(poster(movie_list.iloc[i[0]].id))
    return recommended, movie_posters


def callback_false():
    st.session_state.button_clicked = False


names_movies = movie_list.title
st.title("Movie Recommender System")
movie_selected = st.selectbox('Please search your movie here', names_movies, on_change=callback_false)

if "button_clicked" not in st.session_state:  # Initialize
    st.session_state.button_clicked = False


def callback():
    st.session_state.button_clicked = True


if st.button('Recommend') or st.session_state.button_clicked:
    names, posters = recommend(movie_selected)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        callback()
        st.image(posters[0])
        if st.button(names[0]):
            with st.sidebar:
                col10, col11 = st.columns(2)
                with col10:
                    image(names[0])
                with col11:
                    title(names[0])
                    release(names[0])
                    genres(names[0])
                    keywords(names[0])
                overview(names[0])
                

    with col2:
        callback()
        st.image(posters[1])
        if st.button(names[1]):
            with st.sidebar:
                col10, col11 = st.columns(2)
                with col10:
                    image(names[1])
                with col11:
                    title(names[1])
                    release(names[1])
                    genres(names[1])
                    keywords(names[1])
                overview(names[1])
                

    with col3:
        callback()
        st.image(posters[2])
        if st.button(names[2]):
            with st.sidebar:
                col10, col11 = st.columns(2)
                with col10:
                    image(names[2])
                with col11:
                    title(names[2])
                    release(names[2])
                    genres(names[2])
                    keywords(names[2])
                overview(names[2])
               

    with col4:
        callback()
        st.image(posters[3])
        if st.button(names[3]):
            with st.sidebar:
                col10, col11 = st.columns(2)
                with col10:
                    image(names[3])
                with col11:
                    title(names[3])
                    release(names[3])
                    genres(names[3])
                    keywords(names[3])
                overview(names[3])
                

    with col5:
        callback()
        st.image(posters[4])
        if st.button(names[4]):
            with st.sidebar:
                col10, col11 = st.columns(2)
                with col10:
                    image(names[4])
                with col11:
                    title(names[4])
                    release(names[4])
                    genres(names[4])
                    keywords(names[4])
                overview(names[4])
                

footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by Mohamed Shaad
                &nbsp;
                <a href="https://www.linkedin.com/in/mohamedshaad">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/shaadclt">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
"""
st.markdown(footer, unsafe_allow_html=True)
