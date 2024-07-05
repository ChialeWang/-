from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

# 更新連接字串，使用正確的驅動程序名稱和端口號
connection_string = 'mssql+pyodbc://SA:passw0rd@localhost:1433/database?driver=/usr/lib64/libmsodbcsql-17.so&connect_timeout=30'

# 配置 SQLAlchemy 的數據庫 URI
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db.init_app(app)

class blcomics(db.Model):
    __tablename__ = 'blcomics'
    name = db.Column(db.String(100), primary_key=True)

    def __init__(self, name):
        self.name = name

with app.app_context():
    db.create_all()
print('資料庫連線成功！')
app.run()
