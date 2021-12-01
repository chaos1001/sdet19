from datetime import datetime

from platformHomework.backend.server import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remark = db.Column(db.String(120))
    # 用例执行时间
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # 测试报告url
    report = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "remark": self.remark,
            "created": str(self.created),
            "report": self.report,
        }


if __name__ == '__main__':
    db.create_all()
