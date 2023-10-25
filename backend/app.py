from flask import Flask, send_file
from flask_cors import CORS

import plotly.graph_objects as go

import pandas as pd
import numpy as np

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
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))
    fig.write_image("plotly_plot.png")
    time2 = time.perf_counter()
    if (timingBool):
        with open('timings.txt', 'a') as timings:
            curTime = datetime.datetime.now()
            timings.write(curTime.strftime("%m/%d/%Y, %H:%M:%S") + ": " + str(time2 - time1) + "s\n")
    return send_file("plotly_plot.png", mimetype='image/png')