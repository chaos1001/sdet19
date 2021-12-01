import requests


class TestTask:
    def setup_class(self):
        self.url = "http://127.0.0.1:5000/task"

    def test_get_task(self):
        r = requests.get(self.url)
        assert r.status_code

    def test_post_task(self):
        task_data = [{"id": 1, "nodeid": "test_server.py"}]
        r = requests.post(self.url, json=task_data)
        assert r.status_code
