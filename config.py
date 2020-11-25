# 设置连接数据库参数
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'stu'
USERNAME = 'root'
PASSWORD = 'wasd200016'
DB = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=UTF8MB4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB

# 设置数据库追踪信息,压制警告
SQLALCHEMY_TRACK_MODIFICATIONS = True