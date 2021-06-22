import pytest
import yaml
import logging

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture
def get_calc_obj():
    calc = Calculator()
    logging.info("开始计算")
    yield calc
    logging.info("结束计算")


def get_calc_datas():
    with open("./datas/calc.yml") as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture(params=get_calc_datas()['add']['success']['datas'], ids=get_calc_datas()['add']['success']['ids'])
def get_add_success_datas(request):
    return request.param


@pytest.fixture(params=get_calc_datas()['add']['fail']['datas'], ids=get_calc_datas()['add']['fail']['ids'])
def get_add_fail_datas(request):
    return request.param


@pytest.fixture(params=get_calc_datas()['div']['success']['datas'], ids=get_calc_datas()['div']['success']['ids'])
def get_div_success_datas(request):
    return request.param


@pytest.fixture(params=get_calc_datas()['div']['fail']['datas'], ids=get_calc_datas()['div']['fail']['ids'])
def get_div_fail_datas(request):
    return request.param
