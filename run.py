from app import app
if __name__ == '__main__':
    app.run()


# We import the app instance and check if the script is run directly then use the app.run method to launch the server. 
# We pass in the debug = True argument to allow us to run on debug mode so that we can easily track errors in our application.
# After importing the configurations into the __init__ file, we remove the Debug=True since the debug mode has been enabled in the configuration file.

