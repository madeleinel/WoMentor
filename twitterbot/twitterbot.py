import tweepy

# Use the access key and token generated through the WomenToTech account
auth = tweepy.OAuthHandler("V8g3K2XL8Gu6ar7JQjwgeelMn", "ezPze5ik1oAuyXHpSffh6sZ1Qg0c0GEf6cFI3tpwNH9zpzyQtp")
auth.set_access_token("845260665115885568-N35GJTJiXAtInYVig4qQ0NRy8jpNWy2", "7iUQTqzj6NialEEmk4DML5uESKlgRtFHXt6fhdPTLauoF")

twitter_api = tweepy.API(auth)

# To tweet "Happy Friday evening!":
twitter_api.update_status("Happy Friday evening!")
