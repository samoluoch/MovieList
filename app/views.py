# We now create our index page view function
from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie
from .models import reviews
from .forms import ReviewForm
Review = reviews.Review

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

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
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
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie, reviews = reviews)
# We add a route that has a movie function. The part in the angle brackets <> is dynamic, and any route mapped to this will be passed. 
# This returns a response of movie.html file
# We create a movie object by calling the get_movie() function and pass in the dynamic URL id. We then pass that route into our template file.
# We the import the search_movie() function from the request.py file. We then create the search view function that will display our search items from the API.
# We update our movie view function and call the get_reviews class method that takes in a movie ID and will return a list of reviews for that movie. 
# We then pass in the reviews list to our template

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name_format}'
    return render_template('search.html', movies=searched_movies)


# We create a search view function that passes in a dynamic variable. We then format the movie_name to add +sign between the multiple words.
# We then call the search_movie() and pass in the formatted movie name. We then pass the searched_movies list to our template.

# The request object is provided by flask and it encapusaltes our HTTP request with all its arguments to the view function.



# We update our index view function. When we submit the form inside our index.html it creates a query with the name of the input movie_query and the value as the input value. 
# We get the query in our view function using request.args.get() function. We pass in the name of the query and the value is returned. We then check if the value actually exists.
# If it does we use the redirect function that redirects us to another view function. We then pass in the url_for function that passes in the search view function together with the dynamic movie_name which assign it to our form input value.



@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie', id = movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

# In the above, we add the methods argument to our decorator which tells flask to register the view function as a handler for both GET and POST requests.
# When methods argument is not given, the view function is registered to handle GET requests only. 
# We then create an instance of the ReviewForm class and name it form. We also call the get_movie and pass in the ID to get the movie object for the movie with that ID.
# The validate_on_submit() method returns True when the form is submitted and all the data has been verified by the validators. If True, we gather the data from the form input fields and create a new review object and save it.
# We then redirect the response to the movie view function and pass in dynamic movie ID.
# If the validate_on_submit() returns False, we will render our new_review.html template file and pass in the title, the form object, and the movie object.


