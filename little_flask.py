# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request,redirect
from models import *
from werkzeug.utils import secure_filename
import os
import uuid
import socket
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://irlans:1995813zxc@192.168.1.224/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = '/static'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    info = test.query.all()
    content = {
        'data': info,
    }
    return render_template('index.html', content=content)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        print(request.files.values())
        if request.files.values():
            file1 = request.files['file1']
            file2 = request.files['file2']
            filename1 = secure_filename(file1.filename)
            imgurl1 = str(uuid.uuid4())
            imgurl2 = str(uuid.uuid4())





            file1.save(os.path.join(os.path.dirname(__file__)+'/static/img/pv',imgurl1+'.jpg'))
            file2.save(os.path.join(os.path.dirname(__file__)+'/static/img/pv',imgurl2+'.jpg'))

            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(('192.168.1.112',51005))

            onedata = {
                'dbIndex':'pv',
                'jobType':0,
                'images':[imgurl1+'.jpg',imgurl2+'.jpg']
            }
            s.send(json.dumps(onedata))
            replay = json.loads(s.recv(1024))
            s.close()
            info = ''
            result = replay['result']
            fid = replay['fid']

            print(replay)
            if replay['jobType'] == 0:
                info = 'success'
            elif replay['jobType'] == -1:
                info = 'db error'
            elif replay['jobType'] == -2:
                info = 'feature error'
            elif replay['jobType'] == -3:
                info = 'face rect error'
            elif replay['jobType'] == -4:
                info = 'no face'
            elif replay['jobType'] == -5:
                info = 'file error'


            print(info)



            # img1 = Img(imgname=str(file1.filename),imgurl=imgurl1)
            # img2 = Img(imgname=str(file2.filename),imgurl=imgurl2)
            # db.session.add(img1)
            # db.session.add(img2)
            # db.session.commit()
            #
            # imgpath = Img.query.all()
            content = {
                'info': info,
                'img1':imgurl1+'.jpg',
                'img2':imgurl2+'.jpg',
                'fid':fid+'.jpg',
                'result':'%.2f'%(float(result)*100)
                # 'imginfo':imgpath
            }
            return render_template('upload.html', content=content)
        else:
            return redirect('/upload')



@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/search/<id>')
def search_detail(id):
    rid = id
    return render_template('search.html')


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
