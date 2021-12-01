import json

from flask import request
from flask_restful import Resource

from platformHomework.backend.log_util import logger
from platformHomework.backend.models.testcase_model import TestCase
from platformHomework.backend.server import db


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
