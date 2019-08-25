# 运行脚本文件

# 导入Manage模块
from flask_script import Manager
# 从主app.py中导入app
from app import app
# 从flask_migrate中导入Manager，MigrateCommand
from flask_migrate import Migrate, MigrateCommand
# 从exts中导入db
from exts import db
from models import Users


manager = Manager(app)


# 1.要flask_migrate使用必须先进行app和db绑定
migrate = Migrate(app, db)
# 2.把命令添加到中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()