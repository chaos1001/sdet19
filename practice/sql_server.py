from flask import Flask
from practice.backend.log_util import logger
from flask_sqlalchemy import SQLAlchemy

# 实例化flask，并将app绑定到api类上
app = Flask(__name__)

# 配置数据的地址
username = "root"
pwd = "root_cc"
ip = "127.0.0.1"
port = 3306
database = "ck19"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 绑定app与sqlalchemy
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=False)


if __name__ == '__main__':
    # 根据db.Model新建表
    db.drop_all()
    db.create_all()

    # 新增数据
    user1 = User(id=1, username="张三1", email="123@qq.com", gender="男")
    user2 = User(id=2, username="张三2", email="123@qq.com", gender="男")
    user3 = User(id=3, username="张三3", email="123@qq.com", gender="男")
    user4 = User(id=4, username="张三4", email="123@qq.com", gender="男")
    # 将新数据加入session
    db.session.add(user1)
    # 批量插入
    db.session.add_all([user2, user3, user4])
    # 改动数据库数据的话必须要commit
    db.session.commit()

    # 查询单条
    res = User.query.filter_by(id=1).first()
    logger.info(f"{res.username}, {res.email}, {res.gender}")
    # 查询全部
    res = User.query.all()
    logger.info(res)
    # 只查询指定字段
    res = db.session.query(User.username, User.email, User.gender).filter(User.id == 2).first()
    logger.info(res)

    # 修改
    User.query.filter_by(id=2).update({"gender": "女"})
    # 改动数据库数据的话必须要commit
    db.session.commit()

    # 删除
    User.query.filter_by(id=3).delete()
    # 改动数据库数据的话必须要commit
    db.session.commit()






