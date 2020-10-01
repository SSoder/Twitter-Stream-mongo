import json
from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING as desc

class TweetStore:

    num_tweets = 20

    def __init__(self):
        #mongoDB Configuration
        self.mongo_user = "superuser"
        self.mongo_pass = "Data"
        self.mongo_host = "Localhost:27017/admin"
        self.mongo_auth = "admin"
        self.uri = 'mongodb://%s:%s@%s?authSource=%s' % (quote_plus(self.mongo_user), quote_plus(self.mongo_pass), self.mongo_host, self.mongo_auth)
        print("URI: {}".format(self.uri))

        """self.client = MongoClient(host=self.uri)
        try:
            print(self.client.list_database_names())
            print("Connected to MongoDB Client, ready for data.")
        except ConnectionFailure: 
            print("Sorry, connection failed!")
 #       self.db = self.client.tweet_data
 #       self.collection = self.db.tweet_collection"""
        self.trim_count = 0

        
    
    def insert(self, data):
        self.jdata = json.dumps(data)
        print("jdata: {}".format(self.jdata))
        #self.record = self.collection.insert_one()
        print("jdata \"pushed\" to mongoDB.")
        self.trim_count += 1
        print("Trim Count: {}".format(self.trim_count))

        if self.trim_count > 10:
            print("Trim hit ten, trimming to zero!")
            print("Current Trim Count: {}".format(self.trim_count))
            self.trim_count = 0
            print("Reset Trim Count: {}".format(self.trim_count))

    
    def tweets(self, limit=15):
        tweets = ['THIS IS A TEST']

        """for item in self.collection.find().sort('_id', desc).limit(limit):
            tweet_obj = json.loads(item)
            tweets.append(Tweet(tweet_obj))"""
        return tweets
    