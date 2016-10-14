from tasks import count_words, count_them
from flask import Flask
app = Flask(__name__)

@app.route('/index')
def index():
        return "Count tweets with /count_tweets/api/v1.0/count"

@app.route('/count_tweets/api/v1.0/count', methods=['GET'])
def count_tweets():
        r = count_words.delay()
        return r.get()

@app.route('/count_tweets/api/v1.0/count_them', methods=['GET'])
def counter():
        t = count_them()
        return t
if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
