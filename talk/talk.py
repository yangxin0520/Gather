from flask import Blueprint, render_template

talk_ob = Blueprint('talk', __name__, template_folder='./templates', static_folder='static', static_url_path='/talk/static')


@talk_ob.route('/')
def talk_fc():
    return render_template('talk.html')