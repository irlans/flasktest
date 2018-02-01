# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def creat_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://irlans:1995813zxc@192.168.1.224/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['DEBUG'] = True

    from app.main import auth
    app.register_blueprint(auth)

    db.init_app(app)
    # db.create_all()

    return app