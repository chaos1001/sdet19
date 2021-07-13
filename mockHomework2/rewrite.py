import json

import mitmproxy.http
from mitmproxy import http, ctx


class Rewrite:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "stock/batch/quote.json?" in flow.request.pretty_url:
            ctx.log.info("found quote.json")
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["current"] = 9999999999.995
            data["data"]["items"][0]["quote"]["percent"] = -9999999999.995
            data["data"]["items"][1]["quote"]["current"] = "+0.009"
            data["data"]["items"][1]["quote"]["percent"] = "-0"
            data["data"]["items"][2]["quote"]["current"] = -1234
            data["data"]["items"][2]["quote"]["percent"] = 0
            data["data"]["items"][3]["quote"]["current"] = 10
            data["data"]["items"][3]["quote"]["percent"] = 1234.567
            data["data"]["items"][4]["quote"]["current"] = "null"
            data["data"]["items"][4]["quote"]["percent"] = .01
            data["data"]["items"][5]["quote"]["current"] = "031.2"
            data["data"]["items"][5]["quote"]["percent"] = "-1234e-4"

            flow.response.text = json.dumps(data)


addons = [
    Rewrite()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump((['-p', '7654', '-s', __file__]))
