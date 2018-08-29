from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie
#We import the flask application instance and then import the Python urllib.request module 
# that will help us create a connection to our API URL and send a request to json modules 
# that will format JSON response to a Python dictionary.



# Getting api key
api_key = app.config['MOVIE_API_KEY']

# In the above, we access the app configuration objects by calling the app.config['name_of_object']. We get the API key and the movie URL.

# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

# We create a get_movies() function that takes in a movie category as an argument. 
# We use the .format() method on the base_url and pass in the movie category and the api key. This will replace the {} curly brace placeholders in the base_url with the category and api respectively.
# This creates get_movies_url as the final URL for our API request.
# We then use 'with' as our context manager to send a request using the urllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url.
# We use the read() function to read the response and store it in a get_movies_data variable.
# We then convert the JSON response to a Python dictionary using json.loads function and pass in the get_movies_data variable.
# 'result' is a property in the json response that is a list that contains the movie objects. This property is what we use to check if the response contains any data. 
# If it does, we call a process_results() function that takes in the list dictionary objects and returns a list of movie objects. We then return movie_results which is a list of movie objects.

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

# In the above, we create a function process_results() that takes in a list of dictionaries. We create an empty list movie_results where we will store our newly created movie objects.
# We then loop through our list of dictionaries using the get() method and pass in keys so that we can access the values. Some movie_item may not have poster. This will return and error when trying to create objects.
# So we check if the movie_item has a poster then we create the movie object. We use the values we get to create a new movie object then we append it to our empty list. We then return the list with movie objects.



def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
    
    return movie_object

# In the above, we create a get_movie() function that takes in a movie id and returns a movie object. 
# We create a get_movie_details URL by formatting the base URL with id and API key. We then create a request and load the data and create a movie object.





