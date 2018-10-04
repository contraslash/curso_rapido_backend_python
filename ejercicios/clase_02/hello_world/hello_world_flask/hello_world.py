from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<h1>Hello world</h1><p>asdfg</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
