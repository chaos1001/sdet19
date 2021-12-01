import time

from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:
    BASE_URL = "http://127.0.0.1:8080/"
    USERNAME = "ccyang"
    PASSWORD = "118f69954acf3dbf508d13fd11fe576d76"
    JOB_NAME = "1017_platform_task"

    @classmethod
    def get_version(cls):
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        return jenkins.version

    @classmethod
    def invoke(cls, task):
        """
        构建job
        """
        jenkins = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        job = jenkins.get_job(cls.JOB_NAME)
        first_buildnumber = job.get_last_buildnumber()
        job.invoke(build_params={"task": task})
        # todo 超时退出
        while True:
            finished_buildnumber = job.get_last_buildnumber()
            if finished_buildnumber != first_buildnumber:
                report_path = f"{cls.BASE_URL}job/{cls.JOB_NAME}/{finished_buildnumber}/allure/"
                return report_path
            time.sleep(3)
