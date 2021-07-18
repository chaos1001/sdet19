import threading
import time
import pytest
from faker import Faker


@pytest.fixture
def get_unique_name():
    unique_name = "{}{}".format(int(time.time()), threading.currentThread.__name__)
    return unique_name


@pytest.fixture
def get_unique_user_with_email():
    fake = Faker("zh_CN")
    user_id = "{}{}".format(int(time.time()), threading.currentThread.__name__)
    user_name = fake.name()
    department_id_list = [1]
    # 随机出来的手机号有挺大概率重复，用email基本确保不会重复
    email = "{}-{}".format(user_id, fake.email())
    return user_id, user_name, department_id_list, email


@pytest.fixture
def get_tag_id_from_response(response):
    tagid = response.json().get("tagid")
    return tagid


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
