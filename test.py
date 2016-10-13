#!/usr/bin/python
import os
import requests
save_path = "/home/ubuntu/cloud-c3/proj/tweets"
r = requests.get("http://130.238.29.253:8080/swift/v1/tweets")
for i in r.content.split():
    c = requests.get("http://130.238.29.253:8080/swift/v1/tweets/%s" % i)
    nf = open(os.path.join(save_path, i),"w")
    nf.write(c.content)

