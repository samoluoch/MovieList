# We now create our index page view function
from flask import render_template
from app import app
from .request import get_movies,get_movie

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
# We import the render_template() function that takes in the name of a template file as an argument. 
# It then automatically searches for the template file in our app/templates sub directory
# We then import the app instance from the app folder.
# We create a route decorator @app.route('/') and defined the view function index (). 
# As the response, we use the render_template() function and pass in index.html.
# We can replace the message with the title. We create a variable title and pass it into our
# We import the get_movies() funtion from the request module. We then create a variable popular_movies where we call our get_movies() function and pass in 'popular' as an arguments. We then pass the result from that function call to our template


@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)
# We add a route that has a movie function. The part in the angle brackets <> is dynamic, and any route mapped to this will be passed. 
# This returns a response of movie.html file
# We create a movie object by calling the get_movie() function and pass in the dynamic URL id. We then pass that route into our template file.

