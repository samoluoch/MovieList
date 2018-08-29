import unittest
from .models import Movie

Movie = Movie.Movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behavior of the Movie class
    '''

    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()

# We import the unittest module and the movie module. We then get the Movie class. 
# We then create a test class and inside we define a setUp() method. This will instantiate our Movie class to make the self.new_movie object. We pass in six arguments
# We then define a test case test_instance that uses the isinstance() function that checks if the object self.new_movie is an instance of the Movie class.
