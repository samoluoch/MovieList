import unittest
from app.models import Movie
# Movie = movie.Movie

class MovieTest(unittest.TestCase):
    """
    Test class to tests the behaviour of the movie class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """

        self.new_movie = Movie(1234, 'Python must be crazy', 'A thrilling new python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 1299993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))



