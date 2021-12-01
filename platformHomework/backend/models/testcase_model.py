from platformHomework.backend.server import db


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
