# -*- coding:utf-8 -*-
from flask import render_template,request
from models import StudentInfo, LocationInfo , CameraInfo
from .. import db
import uuid
from werkzeug.utils import secure_filename
from . import auth
import socket
import json

# @auth.route('/')
# def hello_world():
#     return 'Hello World!'

@auth.route('/student',methods=['GET','POST'])
def student_add():
    if request.method == 'GET':
        return render_template('student.html')
    if request.method == 'POST':
        studentinfo = StudentInfo()
        sname = request.form['sname']
        sphoto = request.files['sphoto']
        sid = str(uuid.uuid4())
        message = '学生信息入库成功！'.decode('utf-8')


        if secure_filename(sphoto.filename):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('192.168.1.112',51005))

            filename = str(uuid.uuid1())
            studentinfo.sid = sid
            studentinfo.sname = sname
            studentinfo.sphoto = filename
            db.session.add(studentinfo)

            jsondata = json.dumps(
                {
                    'dbIndex':'studentpic',
                    'jobType':1,
                    'images':[filename]
                }
            )
            try:
                db.session.commit()
                sphoto.save('D:\images\studentpic\\' + filename + '.jpg')
                s.send(jsondata)
                replay = s.recv(1024)
                s.close()
            except Exception as e:
                print(e)
                db.session.rollback()
        else:
            message = '录入失败，请检查图片格式是否有误（以.jpg结尾）'.decode('utf-8')

        content = {
            'message':message
        }
        return render_template('student.html', content=content)


@auth.route('/location',methods = ['GET','POST'])
def locationinfo():
    if request.method == 'GET':
        ltioninfo = LocationInfo.query.order_by('datetime DESC').all()
        content = {
            'ltioninfo':ltioninfo
        }
        return render_template('locationinfo.html',content = content)




# def apprun():
#     db.init_app(app)
#     db.create_all()
#     app.run(host='0.0.0.0')




