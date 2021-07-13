import json

import mitmproxy.http
from mitmproxy import http, ctx


# 在请求发给服务期之前截获，用本地文件当做请求服务端的response返回
class MyMapLocal:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        if "stock/batch/quote.json?" in flow.request.pretty_url:
            with open("quote.json") as f:
                flow.response = http.HTTPResponse.make(200, f.read())


addons = [
    MyMapLocal()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump((['-p', '7654', '-s', __file__]))
