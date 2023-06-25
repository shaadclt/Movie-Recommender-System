# Movie Recommender System
This is a Movie Recommender System built using Streamlit and Python. It recommends similar movies based on user input and displays movie details.

## Installation
1. Clone the repository:

``` shell
git clone https://github.com/shaadclt/Movie-Recommender-System.git
```

2. Navigate to the project directory:

``` shell
cd Movie-Recommender-System
```

3. Install the required dependencies:

``` shell
pip install -r requirements.txt
```

4. Run the application:

``` shell
streamlit run movies.py
```

5. Open your web browser and go to **http://localhost:8501** to access the Movie Recommender System.

## Usage
1. Enter the name of a movie in the search box.

2. Click the "Recommend" button to get a list of recommended movies similar to the selected movie.

3. The recommended movies will be displayed along with their posters.

4. Click on a recommended movie to view its details in the sidebar.

## Credits
* The movie data is sourced from The Movie Database (TMDb).
* The recommender system uses collaborative filtering and cosine similarity.
* The movie posters are retrieved using the TMDb API.

## License
This project is licensed under the MIT License.
