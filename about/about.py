from flask import Blueprint, render_template

about_ob = Blueprint('about', __name__, template_folder='./templates', static_folder='static', static_url_path='/about/static')


@about_ob.route('/')
def about_fc():
    return render_template('about.html')