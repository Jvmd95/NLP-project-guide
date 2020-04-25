#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import OAuthHandler
#import the API keys from the config file.
from config import api_key, api_secret, a_token, a_secret 
import sqlite3
import pandas as pd
import time


# In[ ]:


file_name = 'twitter_search' # file_name.sqlite
db_name = 'tweets'           # database name
search = 'python'            # query or search term
since = '2020-04-24'         #YYYY-MM-DD max 7 days before today!
until = '2020-04-25'         #YYYY-MM-DD
lang = 'en'

# Either import twitter keys from a config file or write them here

#api_key = ''
#api_secret = ''
#a_token = ''
#a_secret = ''


# In[ ]:


conn = sqlite3.connect("{}.sqlite".format(file_name))
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS {} (timestamp REAL, tweet TEXT)".format(db_name))
conn.commit()


# In[ ]:


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(a_token, a_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,
                           q = search,
                           since = since,
                           until = until,
                           lang = lang).items():
    
    c.execute("INSERT INTO {} (timestamp, tweet) VALUES (?, ?)".format(db_name), 
                      (tweet.created_at, tweet.text))
    time.sleep(1)


# In[ ]:


#converting database to dataframe for sanity check

sql = '''select * from {} 
                order by timestamp desc'''.format(db_name)
    
df = pd.read_sql(sql, conn)

conn.close()
    
df

