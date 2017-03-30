import ConfigParser
from acceptedlangs import accepted_langs_normal, accepted_langs_lower
# from dbconnect import session, User, Offer, Skills, Languages
import tweepy

# get keys from config
config = ConfigParser.ConfigParser()
config.readfp(open('twitoauth.cfg'))
consumer_key = config.get('Consumer Keys', 'consumer_key')
consumer_secret = config.get('Consumer Keys', 'consumer_secret')
access_token = config.get('Access Keys', 'access_token')
access_token_secret = config.get('Access Keys', 'access_token_secret')

# setting auth from config
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# constructing our own listener class
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        # status is the tweet object and we will manipulate it here

        print status.text.encode('utf-8')


# creatig an instance of our class at this variable
myStreamListener = MyStreamListener()

# assigning our credentials to the listener
myStream = tweepy.Stream(auth = auth, listener=myStreamListener)

# tracking this tag
myStream.filter(track=['#WomenToTech'])
