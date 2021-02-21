import json
import bson
from configparser import ConfigParser
from urllib.parse import quote_plus
from pymongo import MongoClient 
from pymongo.errors import ConnectionFailure
from pymongo import DESCENDING as desc
from tweet import Tweet

class TweetStore:

    num_tweets = 20

    def __init__(self):
        #mongoDB Configuration imported from *.ini file
        
        print("Obtaining database configuration.\n")
        config_file = r'..\\config\\database.ini'
        config_section = 'mongodb'
        print("Parsing database configuration.\n")
        parser = ConfigParser()
        parser.read(config_file)
        dbconfig = {}
        if parser.has_section(config_section):
            params = parser.items(config_section)
            for param in params:
                dbconfig[param[0]] = str(param[1])
            print("Database configuration established.\n")
        else:
            raise Exception('Section {0} not found in the {1} file'.format(config_section, config_file))
        
        self.uri = 'mongodb://%s:%s@%s?authSource=%s' % (quote_plus(dbconfig['mongo_user']), quote_plus(dbconfig['mongo_pass']), dbconfig['mongo_host'], dbconfig['mongo_auth'])
        #print("URI: {}".format(self.uri))
        self.client = MongoClient(host=self.uri)
        self.db = self.client.tweetdb
        self.collection = self.db.tweets
        self.trim_count = 0
        self.test_cxn()

        
    
    def insert(self, data):
        self.record = self.collection.insert_one(data)
        self.trim_count += 1

        if self.trim_count >= 10:
            self.trim_count = 0

    
    def tweets(self, limit=10):
        tweets = []

        for item in self.collection.find().sort('received_at', desc).limit(limit):
            tweet_obj = item
            tweets.append(Tweet(tweet_obj))
        return tweets
     
    def test_cxn(self):
        try:
            self.db.collection_names()
            print("Connected to MongoDB Client, ready for data.")
        except ConnectionFailure: 
            print("Sorry, connection failed!")



if __name__ == "__main__":
    store = TweetStore()
    store.test_cxn()