import streamlit as st
import requests
import pickle
import lzma

api_key = "328663c183ab4dee463d1288e55a00ae&language=en-US"

movie_list = pickle.load(lzma.open('movies.pickle', 'rb'))


def title(movie_name):
    c = st.container()
    c.title(movie_name)


def image(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    image_link = "https://image.tmdb.org/t/p/w260_and_h390_bestv2" + data['poster_path']
    c = st.container()
    c.image(image_link)


def overview(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    overview_link = data['overview']
    c = st.container()
    c.title("Overview")
    c.caption(overview_link)


def cast(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}/credits?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    actor = 0
    actor_photo = []
    actor_name = []
    actor_movie_name = []
    for i in data['cast']:
        if actor > 7:
            break
        else:
            actor_photo_link = "https://www.themoviedb.org/t/p/w138_and_h175_face" + str(i['profile_path'])
            if 'faceNone' in actor_photo_link:
                continue
            else:
                actor_photo.append(actor_photo_link)
                actor_name.append(i['original_name'])
                actor_movie_name.append(i['character'])
                actor += 1

    st.title("Cast")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        with st.container():
            with st.container():
                st.image(actor_photo[0])
            with st.container():
                st.subheader(actor_name[0])
            with st.container():
                st.caption(actor_movie_name[0])

    with col2:
        with st.container():
            with st.container():
                st.image(actor_photo[1])
            with st.container():
                st.subheader(actor_name[1])
            with st.container():
                st.caption(actor_movie_name[1])

    with col3:
        with st.container():
            with st.container():
                st.image(actor_photo[2])
            with st.container():
                st.subheader(actor_name[2])
            with st.container():
                st.caption(actor_movie_name[2])

    with col4:
        with st.container():
            with st.container():
                st.image(actor_photo[3])
            with st.container():
                st.subheader(actor_name[3])
            with st.container():
                st.caption(actor_movie_name[3])

    with col5:
        with st.container():
            with st.container():
                st.image(actor_photo[4])
            with st.container():
                st.subheader(actor_name[4])
            with st.container():
                st.caption(actor_movie_name[4])

    with col6:
        with st.container():
            with st.container():
                st.image(actor_photo[5])
            with st.container():
                st.subheader(actor_name[5])
            with st.container():
                st.caption(actor_movie_name[5])

    with col7:
        with st.container():
            with st.container():
                st.image(actor_photo[6])
            with st.container():
                st.subheader(actor_name[6])
            with st.container():
                st.caption(actor_movie_name[6])


def reviews(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}/reviews?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    people_review = []
    person_name = []
    total_reviews = len(data['results'])
    review = 0
    for i in data['results']:
        if review >= 3 or review > total_reviews or total_reviews == 0:
            break
        else:
            review_link = "https://www.themoviedb.org/review" + str(i['id'])
            if review_link is None:
                continue
            else:
                person_name.append(i['author'])
                people_review.append(i['content'])
                review += 1

    st.title("Reviews")
    if review == 0:
        st.markdown("*_No reviews available_*")
    else:
        for i in range(0, review):
            with st.container():
                with st.container():
                    st.subheader("Author: {}".format(person_name[i]))
                with st.container():
                    st.caption(people_review[i])


def release(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    release_link = data['release_date']
    runtime = data['runtime']
    c = st.container()
    c.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                    f"border: 3px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                    f"line-height: 1; border-radius: 2px;'>{certification(movie_name)}</span>"
               f" &nbsp; ⚬ &nbsp; {release_link} &nbsp; ⚬ &nbsp;{runtime}min",
                    unsafe_allow_html=True)


def certification(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}/release_dates?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    for i in data['results']:
        if i['iso_3166_1'] == 'US':
            for j in i["release_dates"]:
                certi = j['certification']
                break
    return certi


def keywords(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}/keywords?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    key = []
    for keyword in data['keywords']:
        key.append(keyword['name'])
    st.header("Keywords")
    words = len(key)
    if words > 4:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{key[0]} | {key[1]} | {key[2]} | {key[3]}</span>", unsafe_allow_html=True)

    elif words == 3:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{key[0]} | {key[1]} | {key[2]}</span>", unsafe_allow_html=True)

    elif words == 2:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{key[0]} | {key[1]}</span>", unsafe_allow_html=True)

    elif words == 1:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{key[0]}</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                    f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                    f"line-height: 1; border-radius: 2px;'>No keywords present</span>", unsafe_allow_html=True)


def genres(movie_name):
    index = movie_list[movie_list['title'] == movie_name].index[0]
    movie_id = movie_list['id'][index]
    url = 'https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    genre = []
    for gen in data['genres']:
        genre.append(gen['name'])
    st.header("Genres")
    total_genre = len(genre)
    if total_genre > 4:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{genre[0]} | {genre[1]} | {genre[2]} | {genre[3]}</span>", unsafe_allow_html=True)

    elif total_genre == 3:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{genre[0]} | {genre[1]} | {genre[2]}</span>", unsafe_allow_html=True)

    elif total_genre == 2:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{genre[0]} | {genre[1]}</span>", unsafe_allow_html=True)

    elif total_genre == 1:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                        f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                        f"line-height: 1; border-radius: 2px;'>{genre[0]}</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='display: inline-flex; align-items: center; align-content: center; "
                    f"border: 1px solid rgba(255,255,255,0.6); color: white; padding:0.39rem; "
                    f"line-height: 1; border-radius: 2px;'>No genres present</span>", unsafe_allow_html=True)

