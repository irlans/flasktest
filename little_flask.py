# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request,redirect
from models import *
from werkzeug.utils import secure_filename
import os

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
        if request.files.values():
            file = request.files['file']
            filename = secure_filename(file.filename)
            try:
                img = Img(imgname=file.filename)
                file.save(os.path.join(os.path.dirname(__file__)+'/static/img',filename))
                db.session.add(img)
                db.session.commit()
            except:
                pass
            content = {
                'info': 'success!'
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
