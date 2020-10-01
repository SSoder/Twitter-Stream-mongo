import json
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING as desc
from tweet import Tweet

class TweetStore:

    num_tweets = 20

    def __init__(self):
        #mongoDB Configuration
        mongo_user = "superuser"
        mongo_pass = "Data"
        mongo_host = "Localhost:27017/admin"
        mongo_auth = "admin"
        self.uri = 'mongodb://%s:%s@%s?authSource=%s' % (quote_plus(mongo_user), quote_plus(mongo_pass), mongo_host, mongo_auth)
        print("URI: {}".format(self.uri))

        self.client = MongoClient(host=self.uri)
        self.db = self.client.tweet_data
        self.collection = self.db.tweet_collection
        self.trim_count = 0

        
    
    def insert(self, data):
        self.jdata = json.dumps(data)
        self.record = self.collection.insert_one(self.jdata)
        self.trim_count += 1

        if self.trim_count >= 10:
            self.trim_count = 0

    
    def tweets(self, limit=15):
        tweets = []

        for item in self.collection.find().sort('_id', desc).limit(limit):
            tweet_obj = json.loads(item)
            tweets.append(Tweet(tweet_obj))
        return tweets
     
    def test_cxn(self):
        try:
            print(self.client.list_database_names())
            print("Connected to MongoDB Client, ready for data.")
        except ConnectionFailure: 
            print("Sorry, connection failed!")



if __name__ == "__main__":
    store = TweetStore()
    store.test_cxn()