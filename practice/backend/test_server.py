import requests
from practice.backend.log_util import logger


class TestCase:
    def setup_class(self):
        self.url = "http://127.0.0.1:5000/testcase"

    def test_add(self):
        data = {
            "id": 3,
            "node_id": ["node_id2", "node_id21"],
            "remark": "备注1"
        }
        r = requests.post(self.url, json=data)
        assert r.status_code == 200

    def test_select(self):
        r = requests.get(self.url)
        logger.info(r.json())
        assert r.status_code == 200

        params = {"id": 1}
        r1 = requests.get(self.url, params=params)
        logger.info(r1.json())
        assert r1.status_code == 200

    def test_update(self):
        data = {
            "id": 2,
            "node_id": ["node_id3", "node_id4"]
        }
        r = requests.put(self.url, json=data)
        assert r.status_code == 200

    def test_delete(self):
        data = {"id": 1}
        r = requests.delete(self.url, params=data)
        assert r.status_code == 200