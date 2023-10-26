from flask import Flask, send_file
from flask_cors import CORS

import plotly.graph_objects as go

import numpy as np
import pandas as pd

import time
import datetime

# If true writes graph generation timing to "timings.txt"
timingBool = True

np.random.seed(1)

app = Flask(__name__)
# CORS enabled so react frontend can pull data from python backend
CORS(app)

@app.route('/plot1', methods=["GET"])
def plot1():
    time1 = time.perf_counter() 
    df = pd.read_csv('data.csv')
    fig = go.Figure([go.Scatter(
        x=df['Date'], 
        y=df['Value']
    )])

    fig.write_image("plotly_plot.png", scale=1.0)
    time2 = time.perf_counter()
    if (timingBool):
        with open('timings.txt', 'a') as timings:
            curTime = datetime.datetime.now()
            timings.write(curTime.strftime("%m/%d/%Y, %H:%M:%S") + ": " + str(time2 - time1) + "s\n")
    return send_file("plotly_plot.png", mimetype='image/png')