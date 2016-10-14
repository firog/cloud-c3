from celery import Celery
import os
import json
import requests

app = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')

@app.task
def fetch_tweets():
    save_path = "/home/ubuntu/cloud-c3/proj/tweets"
    r = requests.get("http://130.238.29.253:8080/swift/v1/tweets")
    for i in r.content.split():
        if not os.path.isfile("%s/%s" % (save_path, i)):
            c = requests.get("http://130.238.29.253:8080/swift/v1/tweets/%s" % i)
            nf = open(os.path.join(save_path, i),"w")
            nf.write(c.content)
        
@app.task
def count_words():
    words = ["hen","han","hon","den","det","denna","denne"]
    dic = {}
  #  num_tweets = "tweets"
    for i in words:
        dic[i] = 0
 #   dic[num_tweets] = 0
    for filename in os.listdir("/home/ubuntu/cloud-c3/proj/tweets"):
        f = open("/home/ubuntu/cloud-c3/proj/tweets/%s" % filename,"r")
        for line in f:
            if line.startswith("\n"):
                continue
            else:
                data = json.loads(line)
#                dic[num_tweets] += 1
                if not data['retweeted']:
                    text = data['text']
                    content = text.split()
                    for match in words:
                        if match in content:
                            dic[match] += 1
    return  json.dumps(dic)

@app.task
def count_them():
    count = 0
    for filename in os.listdir("/home/ubuntu/cloud-c3/proj/tweets"):
        f = open("/home/ubuntu/cloud-c3/proj/tweets/%s" % filename,"r")
        for line in f:
            if line.startswith("\n"):
                continue
            else:
                count += 1
    return count
