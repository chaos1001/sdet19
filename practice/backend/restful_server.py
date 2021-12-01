from flask import Flask
from flask_restful import Resource, Api
from practice.backend.log_util import logger

# 实例化flask，并将app绑定到api类上
app = Flask(__name__)
api = Api(app)


class TestCaseServer(Resource):
    def get(self):
        logger.info("get method")
        return {"code": 0, "message": "get success"}

    def post(self):
        logger.info("post method")
        return {"code": 0, "message": "post success"}

    def put(self):
        logger.info("put method")
        return {"code": 0, "message": "update success"}

    def delete(self):
        logger.info("delete method")
        return {"code": 0, "message": "delete success"}


class TaskServer(Resource):
    def get(self):
        logger.info("task get method")


# 绑定资源与路由
api.add_resource(TestCaseServer, "/testcase")
api.add_resource(TaskServer, "/task")


if __name__ == '__main__':
    app.run(debug=True)
