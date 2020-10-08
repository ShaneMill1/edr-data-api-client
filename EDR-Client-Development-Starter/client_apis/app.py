#!/home/MDL/smill/miniconda3/envs/search_engine/bin/python

from flask import jsonify,Flask,render_template, send_from_directory, send_file, request
from flask_cors import *

app = Flask(__name__, static_url_path='/static',static_folder='static')
CORS(app)


@app.route('/')
def icao_position_app():
    return render_template('/position/icao_position_app/index.html')

@app.route('/stations.js')
def stations():
    return send_file('stations.js')

@app.route('/noaa.png')
def noaa_png():
    return send_file('noaa.png')

if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5000,debug=True)
