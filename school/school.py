from flask import Blueprint, render_template

school_ob = Blueprint('school', __name__, template_folder='./templates', static_folder='static', static_url_path='/school/static')


@school_ob.route('/')
def school_fc():
    return render_template('school.html')