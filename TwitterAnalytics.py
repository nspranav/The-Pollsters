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

#%%
def GetUserTimeline(userName):

    tweets = twitter.get_user_timeline(screen_name=userName,tweet_mode='extended',count=200)
    X = [ x['full_text'].replace('\n',' ') for x in tweets]
    maxId = tweets[199]['id'] - 1    
    for i in range(16):
        tweets = twitter.get_user_timeline(screen_name=userName,tweet_mode='extended',count=200,max_id = str(maxId))
        X.extend([x['full_text'].replace('\n',' ') for x in tweets])
        if len(tweets) > 0:
            maxId = tweets[len(tweets)-1]['id'] - 1
    return X



# %%

gop_tweets =  GetUserTimeline('GOP')
dem_tweets =  GetUserTimeline('TheDemocrats')


# %%
def save_tweets(filename, tweets):
    with open(filename, "wb") as file:
        file.write("\n".join(tweets).encode('utf-8'))

# %%
save_tweets('gop.txt',gop_tweets)
save_tweets('dems.txt',dem_tweets)

# %%
BLeeForCongress_tweets = GetUserTimeline('JoeBiden')
save_tweets('test.txt',BLeeForCongress_tweets)

# %%
