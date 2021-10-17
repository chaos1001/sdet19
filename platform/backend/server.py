import json

from flask import Flask, request
from flask_restful import Api, Resource

from platform.backend.log_util import logger
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


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "remark": self.remark,
        }


class TestCaseServer(Resource):
    def get(self):
        case_id = request.args.get("id")
        logger.info(f"received args: {case_id}")
        datas = []
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            if case_data:
                datas = [case_data.as_dict()]
        else:
            case_datas = TestCase.query.all()
            datas = [case_data.as_dict() for case_data in case_datas]
        logger.info(f"case datas: {datas}")
        return {"code": 0, "msg": datas}

    def post(self):
        case_data = request.get_json()
        case_id = case_data.get("id")
        logger.info(f"received: {case_data}")
        exist_case = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"exist case: {exist_case}")
        if not exist_case:
            tc = TestCase(**case_data)
            tc.node_id = json.dumps(case_data.get("node_id"))
            db.session.add(tc)
            db.session.commit()
            logger.info(f"case id: {case_id} added")
            return {"code": 0, "message": f"case id {case_id} add success"}
        return {"code": 4001, "message": f"case id {case_id} exists"}

    def put(self):
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"received: {case_data}")
        exist_case = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"exist case: {exist_case}")
        if exist_case:
            case_data["node_id"] = json.dumps(case_data.get("node_id"))
            TestCase.query.filter_by(id=case_id).update(case_data)
            db.session.commit()
            logger.info(f"case id: {case_id} updated")
            return {"code": 0, "message": f"case id {case_id} update success"}
        return {"code": 4002, "message": f"case id {case_id} not exist"}

    def delete(self):
        case_id = request.args.get("id")
        logger.info(f"received args: {case_id}")
        if not case_id:
            return {"code": 4003, "msg": "case_id must not null"}
        exist = TestCase.query.filter_by(id=case_id).first()
        if exist:
            TestCase.query.filter_by(id=case_id).delete()
            db.session.commit()
            logger.info(f"case_id {case_id} deleted")
            return {"code": 0, "message": f"cast_id {case_id} delete success"}
        return {"code": 4004, "message": f"cast_id {case_id} not exists"}


class TaskServer(Resource):
    def get(self):
        logger.info("task get method")


# 绑定资源与路由
api.add_resource(TestCaseServer, "/testcase")
api.add_resource(TaskServer, "/task")


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
