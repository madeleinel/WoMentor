import ConfigParser
from dbconnect import session, User, Offer, Skills, Languages
from tweetparse import tweetParse

def addUserToDB(mentor, twit_uid, tweet_id, screenname):
    userVar = User(mentor_mentee=mentor, twitter_uid=twit_uid, original_tweet_id=tweet_id, scrn_name=screenname)
    session.add(userVar)
    session.commit()
    return userVar

def addSkills(user, skillist):
    for idx, skill in enumerate(skillist):
        if idx == 0:
            skillVar = Skills(skills_1=skill, skillset=user)
            session.add(skillVar)
            session.commit()
        elif idx == 1:
            skillVar = Skills(skills_2=skill, skillset=user)
            session.add(skillVar)
            session.commit()
        elif idx == 2:
            skillVar = Skills(skills_3=skill, skillset=user)
            session.add(skillVar)
            session.commit()
        elif idx == 3:
            skillVar = Skills(skills_4=skill, skillset=user)
            session.add(skillVar)
            session.commit()

def addLangs(user, langlist):
    for idx, lang in enumerate(langlist):
        if idx == 0:
            langVar = Languages(languages_1=lang, polyglot=user)
            session.add(langVar)
            session.commit()
        elif idx == 1:
            langVar = Languages(languages_2=lang, polyglot=user)
            session.add(langVar)
            session.commit()
        elif idx == 2:
            langVar = Languages(languages_3=lang, polyglot=user)
            session.add(langVar)
            session.commit()
        elif idx == 3:
            langVar = Languages(languages_4=lang, polyglot=user)
            session.add(langVar)
            session.commit()

def addOffer(user, offlist):
    for idx, off in enumerate(offlist):
        if idx == 0:
            offVar = Offer(offer_1=off, useroffer=user)
            session.add(offVar)
            session.commit()
        elif idx == 1:
            offVar = Offer(offer_2=off, useroffer=user)
            session.add(offVar)
            session.commit()
        elif idx == 2:
            offVar = Offer(offer_3=off, useroffer=user)
            session.add(offVar)
            session.commit()

def dbCheck(user_id_str, mentor_mentee):
    dbCheckBool = False
    userList = session.query(User).filter_by(twitter_uid=user_id_str).all()
    for user in userList:
        if user.mentor_mentee == mentor_mentee:
            dbCheckBool = True;
    return dbCheckBool

# mentor = session.query(User).filter_by(="mentor").first()
# mentor_status, langs, skill, offer = tweetParse('#WomenToTech #Mentor -langs: javascript, python, haskell -skill: node.js, d3.js, jinja2 -offering: help getting started')
#
# user_one = addUserToDB(mentor_status, 'tragiccabbage')
# addSkills(user_one, skill)
# addLangs(user_one, langs)
# addOffer(user_one, offer)
