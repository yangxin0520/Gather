from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from models import Users
from exts import db

login_register_ob = Blueprint('login_register', __name__, template_folder='./templates', static_folder='static', static_url_path='/login_register/static')


@login_register_ob.route('/test/', methods=['GET', 'POST'])
def test():
    return jsonify({
        'status': 0,
        'message': '登陆成功'
    })


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
            # 给前端返回json数据
            return jsonify({
                'status': 1,
                'message': '登陆成功'
            })
        else:
            # 给前端返回json数据
            return jsonify({
                'status': 0,
                'message': '登陆失败'
            })


@login_register_ob.route('/register/', methods=['GET', 'POST'])
def register_fc():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        userid = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 将邮箱与数据库已知邮箱数据对比
        user_register = Users.query.filter(Users.email == email).first()
        # 如果已存在该邮箱
        if user_register:
            # 返回json数据
            return jsonify({
                'status': 1,
                'message': '该邮箱已注册'
            })
        # 如果邮箱没有重复，那么继续往下判断两次输入密码
        else:
            if password != password2:
                # 返回json数据
                return jsonify({
                    'status': 2,
                    'message': '两次输入密码不一致'
                })
            else:
                # 如果两次密码输入一致，开始像数据库中插入数据
                user = Users(username=userid, email=email, password=password)
                # 插入命令
                db.session.add(user)
                # 确认插入命令
                db.session.commit()
                # 返回json数据
                return jsonify({
                    'status': 3,
                    'message': '注册成功'
                })


# 注销，销毁session
@login_register_ob.route('/logout/')
def logout_fc():
    # 销毁session命令
    session.clear()
    return redirect(url_for('home.home_fc'))