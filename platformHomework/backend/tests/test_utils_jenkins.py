from ..utils import JenkinsUtils


class TestJenkinsUtils:
    def test_jenkins_version(self):
        print(JenkinsUtils.JenkinsUtils.get_version())

    def test_jenkins_invoke(self):
        task = "test_server.py"
        print(JenkinsUtils.JenkinsUtils.invoke(task))
