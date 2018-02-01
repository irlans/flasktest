# -*- coding:utf-8 -*-
import socket
import json
import pymysql
import uuid


def dbinsert(cid, fid, datetime):
    db = pymysql.connect(host='localhost', user='root', password='1995813zxc', db='test', port=3306)
    cursor = db.cursor()
    lid = str(uuid.uuid4())
    sqlinsert = "INSERT INTO locationinfo(lid, cid, fid, datetime) VALUES (%s,%s,%s,%s)"
    try:
        cursor.execute(sqlinsert, (lid, cid, fid, datetime))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()


# dbinsert("001", "b336aa00-064e-11e8-9835-309c2367f191", "2017-11-20 14:35:49")


#打开摄像头并监控
opendata = {"dbIndex": "01", "jobType": 3, "camera_id": "1", "threshold": 0.8, "max_num": 1,
            "images": ["rtsp://admin:camsZJTC@192.168.1.64:554/MPEG-4/ch1/main/av_stream"],
            "sql": "SELECT fid FROM features"}
jsondata = json.dumps(opendata)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.112', 51005))
s.send(jsondata)
while True:
    recvdata = s.recv(1024)
    try:
        replay = json.loads(recvdata[2:])
        if replay['results']:
            if float(replay['results'][0]['score']) >= 0.8:
                cid = "00"+replay['camera_id']
                datetime = replay['time']
                fid = replay['results'][0]['fid']
                print(cid,datetime,fid)
                dbinsert(cid,fid,datetime)
    except:
        print('摄像头已关闭！')
        s.close()




#关闭摄像头
# closedata = json.dumps({
#     "jobType":4,
#     "camera_id":"1"
# })
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('192.168.1.112',51005))
# s.send(closedata)
# s.close()
# print(s.recv(1024))
