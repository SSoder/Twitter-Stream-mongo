import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING as desc

class TweetStore:

    #mongoDB Configuration
    mongo_user = "superuser"
    mongo_pass = "Data"
    mongo_host = "Localhost"
    mongo_port = 27017
    mongo_dbase = "admin"
    mongo_auth = "admin"

    num_tweets = 20

    def __init__(self):

        self.mongo_login = "{}:{}".format(self.mongo_user, self.mongo_pass)
        self.mongo_hoststring = "{}:{}/{}".format(self.mongo_host,self.mongo_port,self.mongo_dbase)

        self.client = MongoClient("mongodb://{}@{}?authSource={}".format(self.mongo_login,self.mongo_hoststring,self.mongo_auth))
        try:
            print(slef.client.list_database_names())
            print("Connected to MongoDB Client, ready for data.")
        except ConnectionFailure: 
            print("Sorry, connection failed!")
        self.db = self.client.tweet_data
        self.collection = self.db.tweet_collection
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
            tweets.append(tweet_obj)"""
        return tweets
    