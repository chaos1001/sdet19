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


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    # 指定关系
    ut = db.relationship("UserType")


class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    # 指定外键，让 user_type.user_info_id 和 user_info.id 关联
    user_info_id = db.Column(db.Integer, db.ForeignKey("user_info.id"))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    ui1 = UserInfo(name="张三1", age=18)
    ui2 = UserInfo(name="张三2", age=18)
    ui3 = UserInfo(name="张3", age=18)
    db.session.add_all([ui1, ui2, ui3])
    # commit 和 flush 都能跑
    # db.session.flush()
    db.session.commit()

    ut1 = UserType(title="普通用户", user_info_id=ui1.id)
    ut2 = UserType(title="高级用户", user_info_id=ui2.id)
    ut3 = UserType(title="管理员用户", user_info_id=ui3.id)
    db.session.add_all([ut1, ut2, ut3])
    db.session.commit()

    # todo 没有外键关系能不能join？
    data = db.session.query(UserInfo.name, UserInfo.age, UserType.title)\
        .join(UserInfo, UserType.user_info_id == UserInfo.id).filter(UserInfo.name == "张三1").all()
    logger.info(f"{data}")
