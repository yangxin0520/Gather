from flask import Blueprint, render_template

home_ob = Blueprint('home', __name__, template_folder='./templates', static_folder='static', static_url_path='/home/static')


@home_ob.route('/')
def home_fc():
    return render_template('home.html')