from little_flask import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class test(db.Model):
    __tablename__ = 'record'
    rid = db.Column(db.VARCHAR(255), primary_key=True)
    camera_id = db.Column(db.VARCHAR(255))
    record_time = db.Column(db.VARCHAR(255))
    bgimg = db.Column(db.VARCHAR(255))
    imgName = db.Column(db.VARCHAR(255))
    result_face = db.Column(db.Text)
    camera_time = db.Column(db.VARCHAR(255))

    def __repr__(self):
        return '<test %r>' % (self.rid)
