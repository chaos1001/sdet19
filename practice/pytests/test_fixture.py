import pytest
import logging


@pytest.fixture()
def login():
    # fixture默认scope为function
    logging.info("login from module")
    return "token"


@pytest.fixture(scope="module")
def browser_open():
    logging.info("open browser")
    yield
    logging.info("close browser")


class TestFixture1:
    def test_case_no_need_login(self):
        logging.info("test_case_no_need_login")

    def test_case_need_login(self, login):
        # 会在testcase执行前自动执行传入的fixture
        # 如果有同名fixture，根据就近原则起效，优先使用本模块中的fixture，没有再去conftest里找
        logging.info("test_case_need_login")
        # 这里的参数直接就是fixture执行后的返回值
        token = login
        logging.info(token)

    def test_case_with_db(self, db_connect):
        logging.info("test_case_with_db")

    # fixture调用fixture
    def test_case_with_second_fixture(self, second_fixture):
        # fixture可以继续引用fixture
        logging.info("test_case_with_second_fixture")
        assert second_fixture == ["first", "second"]

    # fixture传参
    def test_case_with_fixture_data(self, login_with_data):
        # fixture传参
        logging.info("test_case_with_fixture_data")
        assert "_token" in login_with_data

    # scope
    def test_case_with_browser_1(self, browser_open):
        # scope 为 module 的 fixture，用到时才会执行fixture
        logging.info("test_case_with_browser 1")

    def test_case_no_need_browser(self):
        # 不引用fixture
        logging.info("test_case_no_need_browser")

    @pytest.mark.usefixtures("browser_open")
    def test_case_with_browser_2(self):
        # 用另一种方式引用了fixture，但由于scope为module，第二次调用browser_open时不会执行
        logging.info("test_case_with_browser 2")
        # test case的 exception 不影响 fixture、setup、teardown
        raise Exception("just exception")
