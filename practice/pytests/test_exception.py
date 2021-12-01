import pytest
import logging

@pytest.fixture()
def normal_fixture():
    logging.info("normal_fixture setup")
    yield
    logging.info("normal_fixture teardown")


@pytest.fixture()
def exception_fixture():
    logging.info("exception_fixture setup")
    raise Exception("exception")
    yield
    logging.info("exception_fixture teardown")


def test_case_catch_exception(normal_fixture):
    with pytest.raises(ZeroDivisionError):
        logging.info("test_case_catch_exception")
        assert 1/0


def test_case_catch_no_exception(normal_fixture):
    with pytest.raises(ZeroDivisionError):
        assert 1/1
        logging.info("test_case_catch_no_exception")


def test_fixture_exception(exception_fixture):
    logging.info("test_fixture_exception")
    assert True
