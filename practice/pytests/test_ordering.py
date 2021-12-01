import pytest

@pytest.mark.run(order=1)
def test_1():
    assert True


@pytest.mark.run(order=-2)
def test_2():
    assert True


@pytest.mark.run(order=4)
def test_3():
    assert True


# 当用例里只包含class的时候，setup_class和teardown_class会在整个用例的前后只执行一次
# 但当用例里既包含测试类又包含测试函数时，会在每个类方法的前后都运行一次setup_class和teardown_class
class TestClass:
    def setup(self):
        print("test_setup")

    def teardown(self):
        print("test_down")

    def setup_class(self):
        print("test_class_setup")

    def teardown_class(self):
        print("test_class_down")

    @pytest.mark.run(order=-1)
    def test_class_1(self):
        assert True

    @pytest.mark.run(order=2)
    def test_class_2(self):
        assert True

    @pytest.mark.run(order=3)
    def test_class_3(self):
        assert True
