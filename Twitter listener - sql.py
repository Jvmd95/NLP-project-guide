#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import the API keys from the config file.
from config import api_key, api_secret, a_token, a_secret 
import sqlite3
import pandas as pd


# In[ ]:


file_name = 'twitter' # file_name.sqlite
db_name = 'tweets'    # database name
listening = 'python'  # query you want to search to

# Either import twitter keys from a config file or write them here

#api_key = ''
#api_secret = ''
#a_token = ''
#a_secret = ''


# In[ ]:


conn = sqlite3.connect("{}.sqlite".format(file_name))
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS {} (timestamp REAL, retweet TEXT, quote TEXT, quoted_text TEXT, tweet TEXT)".format(db_name))
conn.commit()


# In[ ]:


# StreamListener class inherits from tweepy.StreamListener and overrides on_status and on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            print(status.id_str)
            # if "retweeted_status" attribute exists, flag this tweet as a retweet.
            is_retweet = hasattr(status, "retweeted_status")

            # check if text has been truncated
            if hasattr(status,"extended_tweet"):
                text = status.extended_tweet["full_text"]
            else:
                text = status.text

            # check if this is a quote tweet.
            is_quote = hasattr(status, "quoted_status")
            quoted_text = ""
            if is_quote:
                # check if quoted tweet's text has been truncated before recording it
                if hasattr(status.quoted_status,"extended_tweet"):
                    quoted_text = status.quoted_status.extended_tweet["full_text"]
                else:
                    quoted_text = status.quoted_status.text
                
            # time of posting in ms
            time_ms = status.timestamp_ms
                
            # inserting tweet values into sqlite database
            c.execute("INSERT INTO {} (timestamp, retweet, quote, quoted_text, tweet) VALUES (?, ?, ?, ?, ?)".format(db_name), 
                      (time_ms, is_retweet, is_quote, quoted_text, text))
        
            # slow down the requests
            time.sleep(1)
        
        except KeyError as e:
            
                print(str(e))
                
        return(True)

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()


# In[ ]:


while True:
    # complete authorization and initialize API endpoint
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(a_token, a_secret)
    api = tweepy.API(auth)

    # initialize stream
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    tags = [listening]
    stream.filter(track=tags)


# In[ ]:


# converting table to dataframe for sanity check
sql = '''select * from {} 
                order by timestamp desc'''.format(db_name)
    
df = pd.read_sql(sql, conn)

conn.close()
    
df

