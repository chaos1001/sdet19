import pytest
import logging


@pytest.fixture()
def login():
    # fixture默认scope为function
    logging.info("login from conftest")


@pytest.fixture()
def db_connect():
    logging.info("db connect")
    # yield前的相当于setup，yield后的相当于teardown
    yield
    logging.info("db disconnect")


@pytest.fixture()
def first_fixture():
    logging.info("first fixture")
    return "first"


@pytest.fixture()
def second_fixture(first_fixture):
    logging.info("second fixture")
    return [first_fixture, "second"]


@pytest.fixture(params=["user_a", "user_b", "user_c"], ids=["a login", "b login", "c login"])
def login_with_data(request):
    # fixture内部可以用request.param来获得外部传进来的params
    _p = request.param
    logging.info("login with {}".format(_p))
    yield "{}_token".format(_p)
    logging.info("logout with {}".format(_p))

