import pytest
import yaml
import logging


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def get_party_data():
    with open("./data/parties.yml") as f:
        data = yaml.safe_load(f)
    return data


@pytest.fixture(params=get_party_data()['add']['success']['datas'], ids=get_party_data()['add']['success']['ids'])
def get_add_party_success_datas(request):
    return request.param


@pytest.fixture(params=get_party_data()['add']['fail']['datas'], ids=get_party_data()['add']['fail']['ids'])
def get_add_party_fail_datas(request):
    return request.param

