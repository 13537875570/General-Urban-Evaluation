
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumerkey='qgEq1bQqaPBtE9MUe9iXjel5J'
consumersecret='gZOzN5oQswfcfqkdTzLd49DgibiCKdVNY2hYuzQakwX4GYCnIR'
accesstoken='2780294182-MvbzCoYYsdiCgr5I2tzT9FSbqObkQhaYfbNlSA9'
accesssecret='kR7TQ3yNkCkArHVwrzxgNUUjGelDejEfJBocMB0gw2ke1'


class listener(StreamListener):

    def on_data(self,data):
        try:
    
            #print (data)
            
            tweet=data.split(',"text":"')[1].split('","source')[0]
            
            print (tweet)
            
            saveThis=str(time.time())+'::'+tweet
            
            
            saveFile=open('twitDB1.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')   
            saveFile.close()
            return True
        except BaseException (e):
            print ('failed ondata,') ,str(e)
            time.sleep(5)
        
        
    def on_error(self,status):
        print (status)
        
auth=OAuthHandler(consumerkey,consumersecret)
auth.set_access_token(accesstoken,accesssecret)

twitterstream=Stream(auth,listener())
twitterstream.filter(track=["car"])
