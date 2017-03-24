from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()
