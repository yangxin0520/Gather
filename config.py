# 开启debug模式

debug = True

# 数据库连接操作
# 数据库链接方法：dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask'

# SQLALCHEMY_DATABASE_URI--连接数据库制指定变量
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

# 这行代码防止报错（不影响的报错）
SQLALCHEMY_TRACK_MODIFICATIONS = False