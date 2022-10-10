from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') #this is for home page defined by '/'
def home():
    return render_template("home.html")