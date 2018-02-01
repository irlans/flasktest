# -*- coding:utf-8 -*-
import json
import socket
closedata = json.dumps({
    "jobType":4,
    "camera_id":"1"
})
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.112',51005))
s.send(closedata)
s.close()
print(s.recv(1024))