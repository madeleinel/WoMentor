from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('postgresql://admin:w0m3nrul3@localhost:5432/womentors')

Session = sessionmaker(bind=engine)
session = Session()
# # now session is a instance of the class Session
# session.execute(...)
Base = declarative_base()

map_table_language = Table('user_language_map_table',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('language_id', Integer, ForeignKey('language.id'))
)

map_table_skill = Table('user_skill_map_table',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('skill_id', Integer, ForeignKey('skill.id'))
)

map_table_offer = Table('user_offer_map_table',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('offer_id', Integer, ForeignKey('offer.id'))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    mentor_mentee = Column(String(100), nullable=False)
    twitter_uid = Column(String(100), nullable=False)
    original_tweet_id = Column(String(100), nullable=False)
    scrn_name = Column(String(20), nullable=False)
    languages = relationship('Language', secondary=map_table_language, backref='users')
    skills = relationship('Skill', secondary=map_table_skill, backref='users')
    offers = relationship('Offer', secondary=map_table_offer, backref='users')

class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, Sequence('language_id_seq'), primary_key=True)
    language = Column(String(100), nullable=False)
    __table_args__ = (
        UniqueConstraint('language'),
    )

class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, Sequence('skill_id_seq'), primary_key=True)
    skill = Column(String(100), nullable=False)
    __table_args__ = (
        UniqueConstraint('skill'),
    )

class Offer(Base):
    __tablename__ = 'offer'
    id = Column(Integer, Sequence('offer_id_seq'), primary_key=True)
    offer = Column(String(100), nullable=False)
    __table_args__ = (
        UniqueConstraint('offer'),
    )
