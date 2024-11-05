from flask import Flask
from flask import jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = {
        "status": "OK",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response), 200