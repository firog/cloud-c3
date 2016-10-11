from celery import Celery

import json


app = Celery('tasks', broker='amqp://guest@localhost//', backend='rpc://')

@app.task
def count_words(file):
	f = open(file,"r")
	words = ["hen","han","hon","den","det","denna","denne"]
        dic = {}
        for i in words:
                dic[i]=0
        for line in f:
                if line.startswith("\n"):
                        continue
                else:
                        data = json.loads(line)
                        if not data['retweeted']:
                                text = data['text']
                                content = text.split()
                                for match in words:
                                        if match in content:
                                                dic[match] += 1
        return  json.dumps(dic)

