class Review:
    all_reviews = []

    def __init__(self,movie_id,ritle,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    

# We create a Review class that has __init__() method that takes in the Movie ID, Review title, Image URL, and the review itself
# We then have the save_review method that appends the review object to a class variable all_reviews that is an empty list. 
# We then have a clear_reviews class method that clears all the items from the list.

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

# We create a new class method get_reviews that takes in an ID. It loops through all the reviews in the all_reviews list and checks for reviews that have the same movie ID as id passed.
# We then append those reviews to a new response list and return that response list.








