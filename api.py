import tasks
from flask import Flask
import json

app = Flask(__name__)

@app.route("/twitter/api")
def count_tweets():
	return count_tweets.delay()	
