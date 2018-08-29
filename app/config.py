class Config:
    '''
    General configuration parent class
    '''
    
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

# We created three classes. The parent Config class contains configurations that are used in both production and development stages. 
# The ProdConfig subclass contains configurations that are used in production stages of our app and inherits from our parent Config class. 
# The DevConfig subclass has configurations used in development stages of our app and inherits from the parent Config class
# Inside the DevConfig subclass, we add DEBUG = True, which enables debug mode in our app.

