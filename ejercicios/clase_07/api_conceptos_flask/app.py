import json

from flask import Flask
from flask.wrappers import Response
from flask.json import jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/status-code/<int:status_code>/")
def status_code(status_code):
    return "Hello World", status_code

@app.route("/status-code/<string:status_code>/")
def status_code_2(status_code):
    return "Hello World Cadema", status_code

@app.route("/plain-response")
def plain_response():
    return Response(
        "{'response': 'Hello World'}",
        status=200,
        headers=dict(),
        content_type="test/plain"
    )


@app.route("/json-response")
def json_response():
    response = dict()
    response["value"] = "hello world"
    return jsonify(response), 200

@app.route("/json-response-2")
def json_response_2():
    response = dict()
    response["value"] = "hello world"
    return Response(json.dumps(response), status=200, content_type="application/json")



if __name__ == "__main__":
    app.run(port=8000, debug=True)