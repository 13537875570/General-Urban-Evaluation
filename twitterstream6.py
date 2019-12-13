import tweepy


import pymongo

import json

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filterKeywords = ['IBM', 'Microsoft', 'Facebook', 'Twitter', 'Apple',        'Google', 'Amazon', 'EBay', 'Diageo',
              'General Motors', 'General Electric', 'Telefonica', 'Rolls Royce', 'Walmart', 'HSBC', 'BP',
              'Investec', 'WWE', 'Time Warner', 'Santander Group']


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        try:
            global conn
            conn = pymongo.MongoClient('localhost', 27017)
            print ("Connected successfully!!!")
            global db
            db = conn.mydb
        except pymongo.errors.ConnectionFailure(e):
            print ("Could not connect to MongoDB: %s" % e)
            conn


    def on_data(self, data):
        datajson = json.loads(data)
        for word in filterKeywords:
            if word in datajson['text']:
                collection = db[word]
                collection.insert(datajson)
                print('Tweet found filtered by ' + word)
            else:
                print('')



    def on_error(self, status_code):
        return True  # Don't kill the stream

    def on_timeout(self):
        return True  # Don't kill the stream


    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))