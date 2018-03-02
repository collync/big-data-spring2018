# API keys - don't want to put them on the internet so hide them using git ignore
# APIs are a set of instructions for getting into things/interacting with things
# This one is for getting into Twitter's database
# On developer website: Only get's a week of tweets, and it's sampling !
# Would be big drain on server and bandwidth; the other reason is that they want you to buy stuff
# Chronic problem: weird psets!

import jsonpickle
import tweepy
import pandas as pd

# pulling twitter into pandas from

import os
os.chdir('week-04')
from twitter_keys import api_key, api_secret

# use a few tweepy functions to setup access; tweepy is just a wrapper
# Create authentication object
# pass api_key and api_secret to create an
# App auth authentication vs user authentication; user can post to twitter;
# APis set rate limits, can't ping the servers too often; throttle the level of access you have; in a 15 minute window
# 450 queries up to 100 tweets every 15 minutes

auth = tweepy.AppAuthHandler(api_key, api_secret)
# wait_on_rate_limit and wait_on_rate_limit_notify are options that tell our API object to automatically wait before passing additional queries if we come up against Twitter's wait limits (and to inform us when it's doing so).
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
# figure out how to time your query so you don't go over your rate limit
# tweepy automates this cause if you don't you get blocked

# create an authorization function:
def auth(key, secret): #passing key and secret
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

# call the function:
api = auth(api_key, api_secret) # this does the same thing as the function

# you want to pull what you want from the website
# will return all the tweets and write it to  a json files
# usually not enought to pull stuff from the internet; it'll return way more than we need and not in the format that we want
# we need to get the stuff and parse it
# define new function:

def get_tweets(
    geo,
    out_file,
    search_term = '', #limit to specific search term
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max: #count out the total number of tweets we've accumulated, starts here if it's true then do try
    try:
      if (max_id <= 0): # of of tweets starts at zero
        if (not since_id):
          new_tweets = api.search( #return tweets using a serach that looks for the following 3 things
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else: # branching statement
          new_tweets = api.search( # this is where we are actuall issuing searches #search for these 4 things
            q = search_term, #q is short for query, search term is for us
            rpp = tweet_per_query, #results per page
            geocode = geo, # calls it's spatial query
            since_id = since_id
          )
      else:
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1)
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
            max_id = str(max_id - 1),
            since_id = since_id
          )
      if (not new_tweets): #goes here after one of the above brances; asks, are there no tweets?
        print("No more tweets found")
        break # if none, stop the function
      for tweet in new_tweets: #for every tweet, do a thing.....
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True: #if it's true, write it to a json file.....
            with open(out_file, 'w') as f: #while the out_file is open and w (writable); pass it to the below line as f
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n') #write ??!?!?!?!?!?!?
      max_id = new_tweets[-1].id #creating memory in the API; max_id is the maximum id of the tweet we got last (each tweet has a unique id); return the last element's id
      tweet_count += len(new_tweets)
      # above it the same as tweet_count = tweet_count + len(new_tweets); addding itself to something else use +=
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets
  #max_id has changed and tweet_max has changed



# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '1mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 200

get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name

 # use a json viewer; google one!
 # two lines will return a data frame

# take all the info bout a tweet and create a Series and put it into a table

 def parse_tweet(tweet):
   p = pd.Series()
   if tweet.coordinates != None:
     p['lat'] = tweet.coordinates['coordinates'][0]
     p['lon'] = tweet.coordinates['coordinates'][1]
   else:
     p['lat'] = None
     p['lon'] = None
   p['location'] = tweet.user.location
   p['id'] = tweet.id_str
   p['content'] = tweet.text
   p['user'] = tweet.user.screen_name
   p['user_id'] = tweet.user.id_str
   p['time'] = str(tweet.created_at)
   return p

tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)
