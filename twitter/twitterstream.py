from configvars import access_token, access_token_secret, consumer_key, consumer_secret
from add_to_db import addUserToDB, addLangs, addSkills, addOffer, dbCheck
from tweetparse import tweetParse
import tweepy

# setting auth from config
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# constructing our own listener class
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        user_id_str = status.user.id_str
        tweet_id_str = status.id_str
        twit_handle = status.user.screen_name
        mentor_mentee, languages,skills, offers = tweetParse(status.text.encode('utf-8'))
        print twit_handle
        #query db for if user exists already as mentor/mentee
        dbCheckBool = dbCheck(user_id_str, mentor_mentee)
        if dbCheckBool == False:
            newUser = addUserToDB(mentor_mentee, user_id_str, tweet_id_str, twit_handle)
            addLangs(newUser, languages)
            addSkills(newUser, skills)
            addOffer(newUser, offers)
            print "User {} added to database as a {}".format(twit_handle, mentor_mentee)
        else:
            print "User already exists!"

# creatig an instance of our class at this variable
myStreamListener = MyStreamListener()

# assigning our credentials to the listener
myStream = tweepy.Stream(auth = auth, listener=myStreamListener)

# tracking this tag
myStream.filter(track=['#WomenToTech'])
