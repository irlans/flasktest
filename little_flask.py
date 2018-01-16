from flask import Flask,render_template
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://irlans:1995813zxc@192.168.1.224/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    info = test.query.all()

    content = {
        'data': info,
    }
    return render_template('index.html',content=content)

if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(host='0.0.0.0',debug = True)
