import pytest
import yaml
import logging


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def get_member_data():
    with open("./data/members.yml") as f:
        data = yaml.safe_load(f)
    return data


# @pytest.fixture(params=get_calc_datas()['add']['success']['datas'], ids=get_calc_datas()['add']['success']['ids'])
# def get_add_success_datas(request):
#     return request.param


@pytest.fixture(params=get_member_data()['add']['fail']['datas'], ids=get_member_data()['add']['fail']['ids'])
def get_add_member_fail_datas(request):
    return request.param

