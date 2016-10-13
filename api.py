from tasks import count_words
from flask import Flask, render_template, send_file, make_response
import matplotlib.pyplot as plt
import plotly.plotly as py
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import prettyplotlib as ppl
app = Flask(__name__)

@app.route('/index')
def index():
        return "Count tweets with /count_tweets/api/v1.0/count"

@app.route('/count_tweets/api/v1.0/count', methods=['GET'])
def count_tweets():
        r = count_words.delay()
        return r.get()

if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
