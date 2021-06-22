import pytest
import allure
import logging


@allure.feature("计算器测试")
class TestCalculator:
    @allure.story("加法测试")
    @allure.title("正常用例: {get_add_success_datas[0]} + {get_add_success_datas[1]} == {get_add_success_datas[2]}")
    @pytest.mark.add
    def test_add(self, get_calc_obj, get_add_success_datas):
        message = "asserting {} + {} == {}".format(get_add_success_datas[0], get_add_success_datas[1], get_add_success_datas[2])
        logging.info(message)
        with allure.step(message):
            assert get_add_success_datas[2] == get_calc_obj.add(get_add_success_datas[0], get_add_success_datas[1])

    @allure.story("加法测试")
    @allure.title("异常用例: {get_add_fail_datas[0]} + {get_add_fail_datas[1]} != {get_add_fail_datas[2]}")
    @pytest.mark.xfail
    def test_add_letter(self, get_calc_obj, get_add_fail_datas):
        message = "asserting {} + {} != {}".format(get_add_fail_datas[0], get_add_fail_datas[1], get_add_fail_datas[2])
        logging.info(message)
        with allure.step(message):
            assert get_add_fail_datas[2] == get_calc_obj.add(get_add_fail_datas[0], get_add_fail_datas[1])

    @allure.story("除法测试")
    @allure.title("正常用例: {get_div_success_datas[0]} / {get_div_success_datas[1]} == {get_div_success_datas[2]}")
    @pytest.mark.div
    def test_div(self, get_calc_obj, get_div_success_datas):
        message = "asserting {} / {} == {}".format(get_div_success_datas[0], get_div_success_datas[1], get_div_success_datas[2])
        logging.info(message)
        with allure.step(message):
            assert get_div_success_datas[2] == get_calc_obj.div(get_div_success_datas[0], get_div_success_datas[1])

    @allure.story("除法测试")
    @allure.title("异常用例: {get_div_fail_datas[0]} / {get_div_fail_datas[1]} == {get_div_fail_datas[2]}")
    @pytest.mark.div
    def test_div_by_zero(self, get_calc_obj, get_div_fail_datas):
        with pytest.raises(eval(get_div_fail_datas[2])):
            message = "asserting {} / {} == {}".format(get_div_fail_datas[0], get_div_fail_datas[1], get_div_fail_datas[2])
            logging.info(message)
            with open("./datas/screenshot.jpg", "rb") as f:
                content = f.read()
                allure.attach(content, "测试图片", attachment_type=allure.attachment_type.PNG)
            with allure.step(message):
                get_calc_obj.div(get_div_fail_datas[0], get_div_fail_datas[1])

