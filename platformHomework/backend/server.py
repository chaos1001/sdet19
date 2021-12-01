import json

from flask import Flask, request
from flask_restful import Api, Resource

from platformHomework.backend.log_util import logger
from flask_sqlalchemy import SQLAlchemy

# 实例化flask，并将app绑定到api类上
app = Flask(__name__)
api = Api(app)

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


# 绑定资源与路由，解决循环引用的问题
def router():
    from platformHomework.backend.apis.task_api import TaskServer
    from platformHomework.backend.apis.testcase_api import TestCaseServer
    api.add_resource(TestCaseServer, "/testcase")
    api.add_resource(TaskServer, "/task")


if __name__ == '__main__':
    # 注册路由
    router()
    app.run(debug=True)
