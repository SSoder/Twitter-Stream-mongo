import tweepy
import datetime
import json
from textblob import TextBlob
from tweet_store import TweetStore



class StreamListener(tweepy.StreamListener):

    def start_stream(self):
        file_path = r'..\\config\\twitter_creds.json'

        lang = ["en"]
        track = [
            "@MadTreeBrewing",
            "@Rhinegeist",
            "@BraxtonBrewCo",
            "@MoerleinLH",
            "@TaftsBrewingCo",
            "#cincy",
            "#COVID19",
            "#pizza"
        ]

        with open(file_path) as apiFile:
            
            twitter_api = json.loads(apiFile.read())
            print("Credentials obtained.\n")

        consumer_key = twitter_api['API Key']
        consumer_secret = twitter_api['API Secret Key']
        access_token = twitter_api['Access Token']
        access_token_secret = twitter_api['Access Token Secret']

        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)
        auth = api.auth
        print("Authentication provided.\n")
        print("Starting Stream...\n")
        stream = tweepy.Stream(auth=auth, listener=self)
        stream.filter(languages=lang, track=track)


    def on_status(self, status):
        store = TweetStore()
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
            print("Grabbed a tweet...\n")
            store.insert(tweet_item)
            print("Tweet inserted into collection.\n")


    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == "__main__":
    stream_listener = StreamListener()
    stream_listener.start_stream()