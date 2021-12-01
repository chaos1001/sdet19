from flask_restful import Resource, request

from platformHomework.backend.log_util import logger
from platformHomework.backend.models.task_model import Task
from platformHomework.backend.server import db
from platformHomework.backend.utils.JenkinsUtils import JenkinsUtils


class TaskServer(Resource):
    def get(self):
        task_list = Task.query.all()
        task_list_data = [task.as_dict() for task in task_list]
        logger.info(f"task datas: {task_list_data}")
        return {"code": 0, "msg": task_list_data}

    def post(self):
        logger.info("post method")
        # 前端传来的是多个用例的列表
        case_datas = request.json
        case_nodeids = [case_data["nodeid"] for case_data in case_datas]
        # todo 先只执行第一条
        report_path = JenkinsUtils.invoke(case_nodeids[0])
        task = Task(remark=case_nodeids[0], report=report_path)
        db.session.add(task)
        db.session.commit()
        db.session.close()
        return {"code": 0, "msg": "add task success"}
