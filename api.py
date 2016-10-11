from tasks import count_words
from flask import Flask
app = Flask(__name__)

@app.route('/index')
def index():
        return "Count tweets"

@app.route('/count_tweets/api/v1.0/count', methods=['GET'])
def count_tweets():
        r = count_words.delay("/home/ubuntu/cloud-c3/proj/tweets/05cb5036-2170-401b-947d-68f9191b21c6")	
        return r.get() 
if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
