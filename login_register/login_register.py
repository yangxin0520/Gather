from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models import Users
from exts import db
# 表单验证
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, DataRequired, EqualTo, Email

login_register_ob = Blueprint('login_register', __name__, template_folder='./templates', static_folder='static', static_url_path='/login_register/static')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('提交')


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password', '密码填入不一致')])
    submit = SubmitField('提交')


@login_register_ob.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        pass
    else:
        userid = request.form.get('username')
        password = request.form.get('password')
        user_login = Users.query.filter(Users.username == userid, Users.password == password).first()
        if user_login:
            session['session_username'] = userid
            return redirect(url_for('home.home_fc'))
        else:
            return '请检测用户名或者密码输入是否正确'
    return render_template('login.html', login_form=login_form)


@login_register_ob.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'GET':
        pass
    else:
        userid = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if register_form.validate_on_submit():
            print(userid)
            user_register = Users.query.filter(Users.email == email).first()
            if user_register:
                return '该邮箱已经注册'
            else:
                user = Users(username=userid, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login_register.login'))
        else:
            flash('输入有误')
    return render_template('register.html', register_form=register_form)


@login_register_ob.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('home.home_fc'))