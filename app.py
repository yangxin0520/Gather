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
from login_register.login_register import login_register_ob


app = Flask(__name__)
app.config.from_object(config)
# 将app与exts中的SQLAlchemy绑定
db.init_app(app)
# 用于session配置
app.config['SECRET_KEY'] = os.urandom(24)
# 蓝图路由部分
app.register_blueprint(home_ob, url_prefix='/')
app.register_blueprint(school_ob, url_prefix='/school')
app.register_blueprint(techn_ob, url_prefix='/techn')
app.register_blueprint(talk_ob, url_prefix='/talk')
app.register_blueprint(latter_ob, url_prefix='/latter')
app.register_blueprint(about_ob, url_prefix='/about')
app.register_blueprint(login_register_ob, url_prefix='/')


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
