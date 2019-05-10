# Import the Twython class

#%% Setup
from twython import Twython
import pandas as pd
import json

APP_KEY = '2i6nqdFSM2nIPKzguOnE6Cjjo'
APP_SECRET = 'bGZJgr52EIrcYsAV33Fm9Eex6iVmrzNA57pPZlLubjagKCkfCf'

twitter = Twython(APP_KEY, APP_SECRET)
ACCESS_TOKEN = '1098820795877355520-HlBC7OXyGDDdRHnO7NpkV3XCpNikyZ'
# save access token in a database or something for later use?


# Load credentials from json file
#with open("twitter_credentials.json", "r") as file:
    #creds = json.load(file)

query = {'q': 'lotr',
         'result_type': 'mixed',
         'count': '100',
         'lang': 'en'}


dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in twitter.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

#%%
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

# Structure data in a pandas DataFrame for easier manipulation