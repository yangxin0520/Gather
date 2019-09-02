from flask import Blueprint, render_template, request, session, redirect, url_for
from models import Users
from exts import db

login_register_ob = Blueprint('login_register', __name__, template_folder='./templates', static_folder='static', static_url_path='/login_register/static')


@login_register_ob.route('/login/', methods=['GET', 'POST'])
def login_fc():
    # 如果请求是GET请求，则跳转页面到login.html
    if request.method == 'GET':
        return render_template('login.html')
    # 如果请求时POST请求，则跳转页面到登陆判断逻辑
    else:
        # 获取前端发送来的用户名和密码
        userid = request.form.get('username')
        password = request.form.get('password')
        # 在数据库进行username和password匹配
        user_login = Users.query.filter(Users.username == userid, Users.password == password).first()
        # 如果都匹配正确
        if user_login:
            # 生成session
            session['session_username'] = userid
            return redirect(url_for('home.home_fc'))
        else:
            return '请检测用户名或者密码输入是否正确'


@login_register_ob.route('/register/', methods=['GET', 'POST'])
def register_fc():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        userid = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # 将邮箱与数据库已知数据对比
        user_register = Users.query.filter(Users.email == email).first()
        # 如果已存在该邮箱
        if user_register:
            return '该邮箱已经被注册'
        # 如果邮箱没有重复，那么继续往下判断两次输入密码
        else:
            if password1 != password2:
                return '两次输入的密码不一样，请检查后输入'
            else:
                # 如果两次密码输入一致，开始像数据库中插入数据
                user = Users(username=userid, email=email, password=password1)
                # 插入命令
                db.session.add(user)
                # 确认插入命令
                db.session.commit()
                # 跳转到登陆界面
                return render_template('login.html')

@login_register_ob.route('/logout/')
def logout_fc():
    session.clear()
    return redirect(url_for('home.home_fc'))