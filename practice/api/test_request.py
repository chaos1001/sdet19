import pytest
import requests
from hamcrest import *
from jsonpath import jsonpath


def test_1():
    r = requests.post('http://httpbin.org/post', data={"data1": ["a", "b", "c"]})
    assert_that(1, close_to(0.5, 0.5))
    assert r.json()['headers']['Host'] == "httpbin.org"

class TestRequest:
    def test_assert(self):
        r = requests.post('http://httpbin.org/post', data={"data1": ["a", "b", "c"]})
        assert_that(1, close_to(0.5, 0.5))
        assert r.json()['headers']['Host'] == "httpbin.org"

    def test_jsonpath(self):
        r = requests.post('http://httpbin.org/post', data={"data1": ["a", "b", "c"]})
        r_json = r.json()
        assert jsonpath(r_json, "$.headers.Host")[0] == "httpbin.org"
        assert jsonpath(r_json, "$..Host")[0] == "httpbin.org"
        assert jsonpath(r_json, "$.form.data1")[0][1] == "b"
        assert jsonpath(r_json, "$..data1")[0][2] == "c"
        assert not jsonpath(r_json, "..data1")


@pytest.mark.parametrize('name', ('赫敏', ' 哈利波特'), ids=['赫敏', ' 哈利波特'])
def test_hook(name):
    print(f"姓名 ： {name}")
