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

    def __repr__(self):
        return "{};{};{};{};{};{};{}".format(self.uid, self.scrn_name, self.original_tweet_id, self.twitter_uid, self.offer, self.languages, self.skills)

class Offer(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    offer_1 = db.Column(db.String(100))
    offer_2 = db.Column(db.String(100))
    offer_3 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    def __repr__(self):
        return "Offer,{},{},{}".format(self.offer_1, self.offer_2, self.offer_3)

class Skills(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    skills_1 = db.Column(db.String(100))
    skills_2 = db.Column(db.String(100))
    skills_3 = db.Column(db.String(100))
    skills_4 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    def __repr__(self):
        return "Skills,{},{},{},{}".format(self.skills_1, self.skills_2, self.skills_3, self.skills_4)

class Languages(db.Model):
    oid = db.Column(db.Integer, primary_key=True)
    languages_1 = db.Column(db.String(100))
    languages_2 = db.Column(db.String(100))
    languages_3 = db.Column(db.String(100))
    languages_4 = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))

    def __repr__(self):
        return "Languages,{},{},{},{}".format(self.languages_1, self.languages_2, self.languages_3, self.languages_4)
