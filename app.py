# encoding = utf-8

from flask import Flask, render_template, redirect, request, session, url_for
# 为下文session产生一个随机数
import os
from exts import db
# 引入配置文件
import config
from models import Users
from home.home import home_ob
from school.school import school_ob
from techn.techn import techn_ob
from talk.talk import talk_ob
from latter.latter import latter_ob
from about.about import about_ob


app = Flask(__name__)
app.config.from_object(config)
# 将app与exts中的SQLAlchemy绑定
db.init_app(app)
# 用于session配置
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(home_ob, url_prefix='/')
app.register_blueprint(school_ob, url_prefix='/school')
app.register_blueprint(techn_ob, url_prefix='/techn')
app.register_blueprint(talk_ob, url_prefix='/talk')
app.register_blueprint(latter_ob, url_prefix='/latter')
app.register_blueprint(about_ob, url_prefix='/about')




@app.route('/login/', methods=['GET', 'POST'])
def login():
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
            return render_template('index2.html')
        else:
            return '请检测用户名或者密码输入是否正确'


@app.route('/register/', methods=['GET', 'POST'])
def register():
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


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))



# 钩子函数
@app.context_processor
def my_context_processor():
    # 获取session
    user_username = session.get('session_username')
    # 如果存在session数据
    if user_username:
        # 将username数据从数据库中取出来
        user = Users.query.filter(Users.username == user_username).first()
        if user:
            # 传递给前端使用
            return {'user': user}
    # 使用context_processor函数必须要提供一个集合，否则报错
    return {}


if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True)
