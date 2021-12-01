import pytest


class TestParametrize:
    @pytest.mark.parametrize("a,b,c", [[1,2,3], [4,5,6], [7,8,9]], ids=["a", "b", "c"])
    def test_cases(self, c, b, a):
        # 这里的参数顺序不影响实际值
        print("{}-{}-{}".format(a, b, c))

    @pytest.mark.parametrize("input_,expect", [["1+2", 3], ["4*5", 20], ["7-8", -1]])
    def test_cases_2(self, input_, expect):
        print("{}={}".format(input_, expect))
        assert eval(input_) == expect

    @pytest.mark.parametrize("username", ["somebody", "anybody", "nobody"])
    @pytest.mark.parametrize("password", ["correctPwd", "wrongPwd"])
    def test_cases_times(self, username, password):
        # 定义多个parametrize会自动组合，类似笛卡尔乘积
        print("{}&{}".format(username, password))

