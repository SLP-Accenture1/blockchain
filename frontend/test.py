import json
from flask import Flask
from flask.json.tag import JSONTag
from flask_cors import CORS, cross_origin
from json import dumps
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/database")
@cross_origin()
def hello_world():
    return json.dumps({"Date": "16/12/2021", "Aircraft": "Airbus A380", "Tach Time (revolutions per minute)": "2400", "Total Time in Service":"30", "Name of logger": "Michael Tomm", "Certificate No. of Technician or Repair Facility": "123456", "Description of Inspections, Tests, Repairs and Alterations": "broken", "Status": "Decommissioned"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)