import requests
import json


def test_post_data_json():
    result = requests.post("http://127.0.0.1:5000/page/post", data=json.dumps({"a": "b", "c": "d"}))
    print(result.text)
    result = requests.post("http://127.0.0.1:5000/page/post", json={"a": "b", "c": "d"})
    print(result.text)
    return
