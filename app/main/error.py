from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_ow_four(error):
    """
    Function to render the 404 error page
    :param error:
    :return:
    """

    return render_template('fourowfour.html'), 404