from flask_sqlalchemy import SQLAlchemy
from cordb import db

map_table = db.Table('user_language_map_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('language_id', db.Integer, db.ForeignKey('language.id'))
)

map_table = db.Table('user_skill_map_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
)

map_table = db.Table('user_offer_map_table',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('offer_id', db.Integer, db.ForeignKey('offer.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, db.Sequence('user_id_seq'), primary_key=True)
    mentor_mentee = db.Column(db.String(100), nullable=False)
    twitter_uid = db.Column(db.String(100), nullable=False)
    original_tweet_id = db.Column(db.String(100), nullable=False)
    scrn_name = db.Column(db.String(20), nullable=False)
    languages = db.relationship('Language', secondary=map_table, backref='users')
    skills = db.relationship('Skill', secondary=map_table, backref='users')
    offers = db.relationship('Offer', secondary=map_table, backref='users')

class Language(db.Model):
    id = db.Column(db.Integer, db.Sequence('language_id_seq'), primary_key=True)
    language = db.Column(db.String(100), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('language'),
    )

class Skill(db.Model):
    id = db.Column(db.Integer, db.Sequence('skill_id_seq'), primary_key=True)
    skill = db.Column(db.String(100), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('skill'),
    )

class Offer(db.Model):
    id = db.Column(db.Integer, db.Sequence('offer_id_seq'), primary_key=True)
    offer = db.Column(db.String(100), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('offer'),
    )
