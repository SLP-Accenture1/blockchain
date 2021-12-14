import json
from types import MethodType
from flask import Flask, request
from flask.json.tag import JSONTag
from flask.templating import render_template
from werkzeug.exceptions import MethodNotAllowed
from flask_cors import CORS, cross_origin
from json import dumps
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/database")
@cross_origin()
def hello_world():
    return json.dumps({"Date": "16/12/2021", "Aircraft": "Airbus A380", "Tach Time (revolutions per minute)": "2400", "Total Time in Service":"30", "Name of logger": "Michael Tomm", "Certificate No. of Technician or Repair Facility": "123456", "Description of Inspections, Tests, Repairs and Alterations": "broken", "Status": "Decommissioned"})


# @app.route("/", methods=["GET", "POST"])
# @cross_origin()
# def log_details():
#     r = requests.get("http://127.0.0.1:3000")
#     print(r)
#     return dumps(r)

@app.route("/", methods=["POST"])
@cross_origin()
def log_details():
    inputs = request.get_json()
    print(inputs)
    return json.dumps(inputs)


# @app.route("/", methods=["POST"])
# @cross_origin()
# def log_details():
#     return render_template("website.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)