import logging

import requests


class BaseApi:
    CORP_ID = "wwb233c1264ce7e17c"
    CORP_SECRET = "OZYrQR6IT2cAna-MfIoClMm9f4ehhNw_cX5_D-ZyTJE"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = self.BASE_URL + f"gettoken?corpid={self.CORP_ID}&corpsecret={self.CORP_SECRET}"
        r = requests.get(url)
        token = r.json().get("access_token")
        logging.info("got token {}".format(token))
        return token

    def send(self, method, url, **kwargs):
        url = "{}{}".format(self.BASE_URL, url)
        logging.info("sending method:{} to url:{}".format(method, url))
        return requests.request(method, url, **kwargs)
