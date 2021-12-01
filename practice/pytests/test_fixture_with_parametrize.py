import pytest
import logging


test_user_data = ['Tom', 'jerry']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    logging.info("logging user: {}".format(user))
    return user


# 用parametrize的indirect参数，将parametrize的argvalues作为参数传入argnames的函数里执行
# 感觉太过复杂实际上不如用yaml等来做数据驱动
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    logging.info("login_r return: {}".format(a))
    assert a in test_user_data

