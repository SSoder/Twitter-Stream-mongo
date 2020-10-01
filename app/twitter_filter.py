import tweepy
import datetime
import json
from textblob import TextBlob
from tweet_store import TweetStore



class StreamListener(tweepy.StreamListener):

    def __init__(self):
        file_path = r'..\\config\\twitter_creds.json'

        with open(file_path) as apiFile:
            twitter_api = json.loads(apiFile.read())

        consumer_key = twitter_api['API Key']
        consumer_secret = twitter_api['API Secret Key']
        access_token = twitter_api['Access Token']
        access_token_secret = twitter_api['Access Token Secret']

        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        self.auth = api.auth
        self.store = TweetStore()


    def on_status(self, status):
        if ('RT @' not in status.text):
            
            blob = TextBlob(status.text)
            sent = blob.sentiment
            polar = sent.polarity
            subjective = sent.subjectivity

            tweet_item = {
                        'id_str' : status.id_str,
                        'text' : status.text,
                        'polarity' : polar,
                        'subjectivity' : subjective,
                        'username' : status.user.screen_name,
                        'name' : status.user.name,
                        'received_at' : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
            self.store.insert(tweet_item)


    def on_error(self, status_code):
        if status_code == 420:
            return False
    
         
    def start_stream(self):
        lang = ["en"]
        track = ["@WarbyParker", "@Bonobos", "@Casper", "@Glossier", "@DollarShaveClub", "@Allbirds", "pizza"]
        stream = tweepy.Stream(auth=self.auth, listener=self)
        stream.filter(languages=lang, track=track)
