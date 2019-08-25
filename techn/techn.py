from flask import Blueprint, render_template

techn_ob= Blueprint('techn', __name__, template_folder='./templates', static_folder='static', static_url_path='/techn/static')


@techn_ob.route('/')
def techn_fc():
    return render_template('techn.html')