from flask import Blueprint, render_template

latter_ob = Blueprint('latter', __name__, template_folder='./templates', static_folder='static', static_url_path='/latter/static')


@latter_ob.route('/')
def latter_fc():
    return render_template('latter.html')