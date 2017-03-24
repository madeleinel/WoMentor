import tweepy

# Use the access key and token generated through the WomenToTech account
auth = tweepy.OAuthHandler("V8g3K2XL8Gu6ar7JQjwgeelMn", "ezPze5ik1oAuyXHpSffh6sZ1Qg0c0GEf6cFI3tpwNH9zpzyQtp")
auth.set_access_token("845260665115885568-N35GJTJiXAtInYVig4qQ0NRy8jpNWy2", "7iUQTqzj6NialEEmk4DML5uESKlgRtFHXt6fhdPTLauoF")

twitter_api = tweepy.API(auth)

# To tweet "Happy Friday evening!":
# twitter_api.update_status("Happy Friday evening!")

# To retweet a tweet with ID 844128496188375041 (one of Madde's)
# twitter_api.retweet(844128496188375041)

# To print within the command line: the user name of the authors for the 15 most recent tweets featuring the term "womentor"
# wtt_tweets = twitter_api.search( q="womentor" )
# for tweet in wtt_tweets:
#     print "tweet by " + tweet.user.name
