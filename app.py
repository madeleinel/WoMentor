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
    mentordict = [{ "twitterhandle": "fluffyunicorn", "languages": "javascript, python, ruby", "skills": "tight-rope walking, laughter", "offers": "getting started, happy unicorns", "originaltweet": "http://twitter.com/anyuser/status/203490203491094", "twitterprofile": "https://twitter.com/intent/user?user_id=23492" }, { "twitterhandle": "madeilenel", "languages": "javascript, python", "offers": "getting started, fika", "skills": "tea breaking, cartwheels", "originaltweet": "http://twitter.com/anyuser/status/203490203491094", "twitterprofile": "https://twitter.com/intent/user?user_id=23492" }]
    # TO DO: adapt this to work with multiple offers/languages/etc by making a string out of them
    return render_template("menteeList.html", nomentees=False, menteelist=mentordict)

# to show a list of mentors, temporary placement just so i can test stuff
@app.route("/mentors")
def showMentorList():
    mentordict = [{ "twitterhandle": "fluffyunicorn", "languages": "javascript, python, ruby", "skills": "tight-rope walking, laughter", "offers": "getting started, happy unicorns", "originaltweet": "http://twitter.com/anyuser/status/203490203491094", "twitterprofile": "https://twitter.com/intent/user?user_id=23492" }, { "twitterhandle": "madeilenel", "languages": "javascript, python", "offers": "getting started, fika", "skills": "tea breaking, cartwheels", "originaltweet": "http://twitter.com/anyuser/status/203490203491094", "twitterprofile": "https://twitter.com/intent/user?user_id=23492" }]
    # TO DO: adapt this to work with multiple offers/languages/etc by making a string out of them
    return render_template("mentorList.html", nomentors=False, mentorlist=mentordict)

if __name__ == "__main__":
    app.run()
