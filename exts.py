# encoding = utf-8
# 解决循环引用问题


# 导入SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# 创建一个SQLAlchemy，并对SQLAlchemy进行初始化，SQLAlchemy初始化必须与app进行绑定
db = SQLAlchemy()