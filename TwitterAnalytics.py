#%%
#!pip install twython
#%%
from twython import Twython
import numpy as np 
import os

# %%

APP_KEY = os.getenv('TWITTER_APP_KEY')
APP_SECRET = os.getenv('TWITTER_APP_SECRET')
OAUTH_TOKEN = os.getenv('TWITTER_OAUTH_TOKEN')
OAUTH_TOKEN_SECRECT = os.getenv('TWITTER_OAUTH_TOKEN_SECRECT')

twitter  = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRECT)

# %%
gop_tweets = [x['full_text'].replace('\n',' ') for x in 
twitter.get_user_timeline(screen_name='GOP', tweet_mode = 'extended', count = 500)]
dem_tweets = [x['full_text'].replace('\n',' ') for x in 
twitter.get_user_timeline(screen_name='TheDemocrats',tweet_mode='extended', count=500)]


# %%
def save_tweets(filename, tweets):
    with open(filename, "wb") as file:
        file.write("\n".join(tweets).encode('utf-8'))

# %%
save_tweets('gop.txt',gop_tweets)
save_tweets('dems.txt',dem_tweets)

# %%

