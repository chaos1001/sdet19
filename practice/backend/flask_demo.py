from flask import Flask, request

app = Flask(__name__)


# methods 参数指定接口允许的请求方式
@app.route("/page/get", methods=["get", "post"])
def page_get():
    return f"{request.args.get('a')}"


@app.route("/page/post", methods=["post"])
def page_post():
    return request.json


if __name__ == '__main__':
    # debug模式
    # 启动flask
    app.run(debug=True)
