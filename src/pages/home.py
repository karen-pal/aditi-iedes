from flask import Blueprint, render_template
from models import Page

home = Blueprint("home", __name__)

@home.route("/")
@home.route("/home.html")
def home_main():
    #TODO: page = Page.query.all().first() 
    return render_template('home.html')

