class Movie:
    '''
    Movie class to define Movie objects
    '''

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count


# We define a movie class and then create an __init__ method and pass in the six parameters we want inside our movie objects.

