from configvars import database_url
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
session = Session()
# # now session is a instance of the class Session
# session.execute(...)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    uid = Column(Integer, primary_key=True)
    mentor_mentee = Column(String(100), nullable=False)
    twitter_uid = Column(String(100), nullable=False)
    original_tweet_id = Column(String(100), nullable=False)
    scrn_name = Column(String(20), nullable=False)
    offer = relationship('Offer', backref='useroffer', lazy='dynamic')
    skills = relationship('Skills', backref='skillset', lazy='dynamic')
    languages = relationship('Languages', backref='polyglot', lazy='dynamic')

class Offer(Base):
    __tablename__ = 'offer'
    oid = Column(Integer, primary_key=True)
    offer_1 = Column(String(100))
    offer_2 = Column(String(100))
    offer_3 = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.uid'))

class Skills(Base):
    __tablename__ = 'skills'
    oid = Column(Integer, primary_key=True)
    skills_1 = Column(String(100))
    skills_2 = Column(String(100))
    skills_3 = Column(String(100))
    skills_4 = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.uid'))

class Languages(Base):
    __tablename__ = 'languages'
    oid = Column(Integer, primary_key=True)
    languages_1 = Column(String(100))
    languages_2 = Column(String(100))
    languages_3 = Column(String(100))
    languages_4 = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.uid'))

# a_newuser = User(mentor_mentee="mentor", twitter_handle="faketwitterhandle")
# session.add(a_newuser)
# session.commit()
