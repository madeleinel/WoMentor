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

# to show the Mentee sign-up page when on the "/mentee_signup" URL
@app.route("/mentee_signup")
def showMenteeSignup():
    return render_template("menteeSignup.html")

# to show the Mentor sign-up page when on the "/mentor_signup" URL
@app.route("/mentor_signup")
def showMentorSignup():
    return render_template("mentorSignup.html")

# to show a list of mentors, temporary placement just so i can test stuff
@app.route("/mentors")
def showMentorList():
    mentor = db.session.query(User).filter_by(mentor_mentee="mentor").first()
    print mentor.uid
    print mentor.twitter_handle
    # mentordict = [{ "twitter": "fluffyunicorn", "languages": "javascript", "offer": "gestting started" }, { "twitter": "sallyjane", "languages": "haskell", "offer": "career advice"}]
    # TO DO: adapt this to work with multiple offers/languages/etc by making a string out of them
    return render_template("mentorlist.html", nomentors=True)
    # False, mentorlist=mentordict)

if __name__ == "__main__":
    app.run()
