from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "This app is deployed using CICD pipeline docker image."

@app.route("/hi")
def hello():
    return "This route was added to check whether pipeline is getting triggered or not."

@app.route("/testing")
def test():
    return "Again this is a route for pipeline testing."

@app.route("/info")
def info():
    return jsonify({
        "app": "python-demo",
        "version": "v1",
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
