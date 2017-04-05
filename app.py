import ConfigParser
from cordb import db
from flask import Flask, render_template
from flask_data_models import User, Offer, Languages, Skills
from flask_sqlalchemy import SQLAlchemy


# config importing
config = ConfigParser.ConfigParser()
config.readfp(open('dbcnnct.cfg'))
username = config.get('PostgresDB', 'user')
password = config.get('PostgresDB', 'password')
portnum = config.get('PostgresDB', 'port')
dbname = config.get('PostgresDB', 'dbname')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(username, password, portnum, dbname)
db.init_app(app)

def create_app():
    db.init_app(app)
    return app

# to publish the main page
@app.route("/")
def main():
    return render_template("index.html")

# to show the About page when on the "/about" URL
@app.route("/about")
def showAboutPage():
    return render_template("about.html")

# to show the Mentee sign-up page when on the "/mentee_signup" URL
@app.route("/mentee_signup")
def showMenteeSignup():
    return render_template("signup.html")

# to show the Mentor sign-up page when on the "/mentor_signup" URL
@app.route("/mentor_signup")
def showMentorSignup():
    return render_template("signup.html")

##### for the profile pages: details & db paths need to be updated once the database is done

# to show a list of all mentee profiles
@app.route("/mentees")
def showMenteeList():
    # mentee = db.session.query(User).filter_by(mentor_mentee="mentee").first()
      # print mentee.uid
      # print mentee.scrn_name
      mentee_list = []
      allMentors = db.session.query(User).filter_by(mentor_mentee="mentee").all()
      for mentee in allMentors:
          menteedict = {}
          menteedict['twitterhandle'] = mentee.scrn_name
          menteedict['user_id'] = "https://twitter.com/intent/user?user_id=" + mentee.twitter_uid
          menteedict['originaltweet'] = "http://twitter.com/anyuser/status/" + mentee.original_tweet_id
          languageList = []
          languageString = ""
          languageObjList = mentee.languages
          for langObj in languageObjList:
              languageList.append(checkIsntNone(langObj.languages_1))
              languageList.append(checkIsntNone(langObj.languages_2))
              languageList.append(checkIsntNone(langObj.languages_3))
              languageList.append(checkIsntNone(langObj.languages_4))
          languageList = checkListItems(languageList, [])
          languageString = makeNormalString(languageList, languageString)
          menteedict['languages'] = languageString
          skillList = []
          skillString = ""
          skillObjList = mentee.skills
          for langObj in skillObjList:
              skillList.append(checkIsntNone(langObj.skills_1))
              skillList.append(checkIsntNone(langObj.skills_2))
              skillList.append(checkIsntNone(langObj.skills_3))
              skillList.append(checkIsntNone(langObj.skills_4))
          skillList = checkListItems(skillList, [])
          skillString = makeNormalString(skillList, skillString)
          menteedict['skills'] = skillString
          offerList = []
          offerString = ""
          offerObjList = mentee.offer
          for langObj in offerObjList:
              offerList.append(checkIsntNone(langObj.offer_1))
              offerList.append(checkIsntNone(langObj.offer_2))
              offerList.append(checkIsntNone(langObj.offer_3))
          offerList = checkListItems(offerList, [])
          offerString = makeNormalString(offerList, offerString)
          menteedict['offers'] = offerString
          mentee_list.append(menteedict)
      if len(mentee_list) > 0:
          return render_template("menteelist.html", nomentees=False, menteelist=mentee_list)
      else:
          return render_template("menteelist.html", nomentees=True)

# to show a list of mentors, temporary placement just so i can test stuff
@app.route("/mentors")
def showMentorList():
    # mentor = db.session.query(User).filter_by(mentor_mentee="mentor").first()
    # print mentor.uid
    # print mentor.scrn_name
    mentor_list = []
    allMentors = db.session.query(User).filter_by(mentor_mentee="mentor").all()
    for mentor in allMentors:
        mentordict = {}
        mentordict['twitterhandle'] = mentor.scrn_name
        mentordict['user_id'] = "https://twitter.com/intent/user?user_id=" + mentor.twitter_uid
        mentordict['originaltweet'] = "http://twitter.com/anyuser/status/" + mentor.original_tweet_id
        languageList = []
        languageString = ""
        languageObjList = mentor.languages
        for langObj in languageObjList:
            languageList.append(checkIsntNone(langObj.languages_1))
            languageList.append(checkIsntNone(langObj.languages_2))
            languageList.append(checkIsntNone(langObj.languages_3))
            languageList.append(checkIsntNone(langObj.languages_4))
        languageList = checkListItems(languageList, [])
        languageString = makeNormalString(languageList, languageString)
        mentordict['languages'] = languageString
        skillList = []
        skillString = ""
        skillObjList = mentor.skills
        for langObj in skillObjList:
            skillList.append(checkIsntNone(langObj.skills_1))
            skillList.append(checkIsntNone(langObj.skills_2))
            skillList.append(checkIsntNone(langObj.skills_3))
            skillList.append(checkIsntNone(langObj.skills_4))
        skillList = checkListItems(skillList, [])
        skillString = makeNormalString(skillList, skillString)
        mentordict['skills'] = skillString
        offerList = []
        offerString = ""
        offerObjList = mentor.offer
        for langObj in offerObjList:
            offerList.append(checkIsntNone(langObj.offer_1))
            offerList.append(checkIsntNone(langObj.offer_2))
            offerList.append(checkIsntNone(langObj.offer_3))
        offerList = checkListItems(offerList, [])
        offerString = makeNormalString(offerList, offerString)
        mentordict['offers'] = offerString
        mentor_list.append(mentordict)
    if len(mentor_list) > 0:
        return render_template("mentorlist.html", nomentors=False, mentorlist=mentor_list)
    else:
        return render_template("mentorlist.html", nomentors=True)

def checkIsntNone(item):
    if item != None:
        return item.encode('utf-8')
    else:
        return 'None'

def checkListItems(list,final_list):
    for item in list:
        if item != 'None':
            final_list.append(item)
    return final_list

def makeNormalString(list, string):
    firstIteration = True
    for i, item in enumerate(list):
        if i == len(list) - 1:
            if firstIteration == True:
                string += " {}.".format(item)
            else:
                string += "and {}.".format(item)
        elif i < len(list) - 2:
            string += "{}, ".format(item)
            firstIteration = False
        elif i == len(list) - 2:
            string += "{} ".format(item)
            firstIteration = False
        elif "and more" in item:
            string += " {}".format(item)
            firstIteration = False
    return string

def makeString(list):
  str = ", ".join(list)
  idx = str.rfind(',')
  str = str[:idx] + " and " + str[idx+2:]
  # Case of 'and more' still needs considering !!!!!
  return str

if __name__ == "__main__":
    app.run(debug=True)
