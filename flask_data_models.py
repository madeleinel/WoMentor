from flask_sqlalchemy import SQLAlchemy
from cordb import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    mentor_mentee = db.Column(db.String(100), nullable=False)
    twitter_uid = db.Column(db.String(100), nullable=False)
    original_tweet_id = db.Column(db.String(100), nullable=False)
    scrn_name = db.Column(db.String(20), nullable=False)
    offer = db.relationship('Offer', backref='useroffer', lazy='dynamic')
    skills = db.relationship('Skills', backref='skillset', lazy='dynamic')
    languages = db.relationship('Languages', backref='polyglot', lazy='dynamic')

class Offer(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    offer_1 = db.Column(db.String(100))
    offer_2 = db.Column(db.String(100))
    offer_3 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

class Skills(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    skills_1 = db.Column(db.String(100))
    skills_2 = db.Column(db.String(100))
    skills_3 = db.Column(db.String(100))
    skills_4 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

class Languages(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    languages_1 = db.Column(db.String(100))
    languages_2 = db.Column(db.String(100))
    languages_3 = db.Column(db.String(100))
    languages_4 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
