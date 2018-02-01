# -*- coding:utf-8 -*-
from .. import db


class StudentInfo(db.Model):
    __tablename__ = 'StudentInfo'
    sid = db.Column(db.VARCHAR(50), primary_key=True)
    sname = db.Column(db.VARCHAR(20))
    sphoto = db.Column(db.VARCHAR(50))

    def __repr__(self):
        return '<studentinfo %r>' % (self.sname)


class CameraInfo(db.Model):
    __tablename__ = 'camera'
    cid = db.Column(db.VARCHAR(64), primary_key=True)
    cadress = db.Column(db.VARCHAR(64))
    curl = db.Column(db.VARCHAR(255))
    cstatus = db.Column(db.Integer)
    matched_num = db.Column(db.Integer)
    matched_score = db.Column(db.Integer)

    def __repr__(self):
        return '<CameraInfo %r>' % (self.cid)


class LocationInfo(db.Model):
    __tablename__ = 'locationinfo'
    lid = db.Column(db.VARCHAR(50), primary_key=True)
    cid = db.Column(db.VARCHAR(64), db.ForeignKey('camera.cid'))
    fid = db.Column(db.VARCHAR(50), db.ForeignKey('StudentInfo.sphoto'))
    datetime = db.Column(db.DateTime)
    sinfo = db.relationship('StudentInfo')
    cinfo = db.relationship('CameraInfo')

    def __repr__(self):
        return '<Locationinfo %r>' % (self.fid)
