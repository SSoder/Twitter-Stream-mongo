import json
from pymongo import MongoClient

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

        mongo_login = "{}:{}".format(self.mongo_user, self.mongo_pass)
        mongo_hoststring = "{}:{}/{}".format(self.mongo_host,self.mongo_port,self.mongo_dbase)

        self.Client = MongoClient("mongodb://{}@{}?authSource={}".format(self.mongo_login,self.mongo_hoststring,self.mongo_auth))
        try:
            self.Self.client == True
            print("Connected to MongoDB Client, ready for data.")
        except: 
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
        tweets = []

        for item in self.collection.find().sort([_id:-1]).limit(limit):
            tweet_obj = json.loads(item)
            tweets.append(tweet_obj)
        return tweets
    