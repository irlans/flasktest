# -*- coding:utf-8 -*-
from flask.ext.script import Manager
from app import creat_app

app = creat_app()
app.host = '0.0.0.0'
manager = Manager(app)



if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    manager.run()