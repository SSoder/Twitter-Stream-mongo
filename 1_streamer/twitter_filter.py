import tweepy
from textblob import TextBlob
import datetime
import json


file_path = '..\config\\twitter_creds.json'

with open(file_path) as apiFile:
    twitter_api = json.loads(apiFile.read())

consumer_key = twitter_api['API Key']
consumer_secret = twitter_api['API Secret Key']
access_token = twitter_api['Access Token']
access_token_secret = twitter_api['Access Token Secret']

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        if ('RT @' not in status.text):
            tweets = 0
            with open('..\output\\tweets.json', 'w') as outfile:
                while tweets < 5:
                    tweet_item = {
                        'id_str' : status.id_str,
                        'text' : status.text,
                        'username' : status.user.screen_name,
                        'name' : status.user.name,
                        'received_at' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    json.dump(tweet_item, outfile)
                    tweets += 1
                
                
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["@WarbyParker", "@Bonobos", "@Casper", "@Glossier", "@DollarShaveClub", "@Allbirds", "pizza"])
