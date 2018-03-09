import jsonpickle
import tweepy
import pandas as pd
import os
os.listdir()
os.chdir('week-04')
from twitter_keys import api_key, api_secret

def auth(key, secret):
  auth = tweepy.AppAuthHandler(key, secret)
  api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
  # Print error and exit if there is an authentication error
  if (not api):
      print ("Can't Authenticate")
      sys.exit(-1)
  else:
      return api

api = auth(api_key, api_secret)

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


def get_tweets(
    geo,
    out_file,
    search_term = '',
    tweet_per_query = 100,
    tweet_max = 150,
    since_id = None,
    max_id = -1,
    write = False
  ):
  tweet_count = 0
  all_tweets = pd.DataFrame()
  while tweet_count < tweet_max:
    try:
      if (max_id <= 0):
        if (not since_id):
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo
          )
        else:
          new_tweets = api.search(
            q = search_term,
            rpp = tweet_per_query,
            geocode = geo,
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
      if (not new_tweets):
        print("No more tweets found")
        break
      for tweet in new_tweets:
        all_tweets = all_tweets.append(parse_tweet(tweet), ignore_index = True)
        if write == True:
            with open(out_file, 'w') as f:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
      max_id = new_tweets[-1].id
      tweet_count += len(new_tweets)
    except tweepy.TweepError as e:
      # Just exit if any error
      print("Error : " + str(e))
      break
  print (f"Downloaded {tweet_count} tweets.")
  return all_tweets

# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# set output file location
file_name = 'data/tweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

tweets = get_tweets(
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

#HAVE TO RUN THIS AFTER RUNNING THE CODE :<
tweets.to_json('data/tweets.json')

#Check how many tweets etc.
tweets.shape
tweets.head()


####### Part 2 #######
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#Load into the dataframe
df = pd.read_json('data/tweets.json')
df.head()

#df['lon'].unique()

# Don't need to remove duplicates, since RT does not duplicate location
# tweets[tweets.duplicated(subset = 'content', keep = False)]
# tweets.drop_duplicates(subset = 'content', keep = False, inplace = True)

#Cleaning the locations

boston_list = df[df['location'].str.contains("Boston", case=False)]['location']
df['location'].replace(boston_list, 'Boston, MA', inplace = True)

#check that it's been replaced
# boston_list.value_counts()
df['location'].value_counts()

cambridge_list = df[df['location'].str.contains("Cambridge", case=False)]['location']
canada_list = df[df['location'].str.contains("Canada", case=False)]['location']
mass_list = df[df['location'].str.contains("Massachusetts", case=False)]['location']
usa_list = df[df['location'].str.contains("United States", case=False)]['location']
brookline_list = df[df['location'].str.contains("Brookline", case=False)]['location']
houston_list = df[df['location'].str.contains("Houston", case=False)]['location']
medford_list = df[df['location'].str.contains("Medford", case=False)]['location']
ny_list = df[df['location'].str.contains("New York", case=False)]['location']
sville_list = df[df['location'].str.contains("Somerville", case=False)]['location']
wb_list = df[df['location'].str.contains("Woodbridge", case=False)]['location']
cali_list = df[df['location'].str.contains("California", case=False)]['location']

df['location'].replace(cambridge_list, 'Cambridge, MA', inplace = True)
df['location'].replace(canada_list, 'Canada', inplace = True)
df['location'].replace(mass_list, 'Massachusetts', inplace = True)
df['location'].replace(usa_list, 'USA', inplace = True)
df['location'].replace(brookline_list, 'Brookline, MA', inplace = True)
df['location'].replace(houston_list, 'Houston, TX', inplace = True)
df['location'].replace(medford_list, 'Medford, MA', inplace = True)
df['location'].replace(ny_list, 'New York, NY', inplace = True)
df['location'].replace(sville_list, 'Somerville, MA', inplace = True)
df['location'].replace(wb_list, 'Woodbridge, MA', inplace = True)
df['location'].replace(cali_list, 'Somewhere in California', inplace = True)

df['location'].value_counts()

#Remove missing tweet locations
cleaner_tweets=df[df['location'] != ""]
cleaner_tweets['location'].value_counts()

cleaner_tweets

#Take only the cleaned up locations, which are all locations that have a count greater than 5
#Put value counts of locations into a new data frame
location_count_frame= cleaner_tweets['location'].value_counts().to_frame()
location_count_frame.head()
#Take locations with counts over 10 and place into another variable
q2_pie = location_count_frame[location_count_frame['location']>10]
q2_pie
q2_pie.shape

#Plotting the pie chart

colors = ["#d84577","#4eacd7",
          "#cf4e33","#894ea8","#cf8c42","#d58cc9",
          "#737632","#9f4b75","#c36960"]

plt.pie(q2_pie['location'], labels=q2_pie['location'].get_values(),  shadow=False, colors=colors)
plt.title('Self-Reported Tweet Locations within 5 mile Radius of Erics Office')
plt.axis('equal')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), labels=q2_pie['location'].keys())
plt.tight_layout()
plt.show()

# df.dtypes
# df['location'].unique()
# loc_tweets = tweets[tweets['location'] != '']
# count_tweets = loc_tweets.groupby('location')['id'].count()
# df_count_tweets = count_tweets.to_frame()
# df_count_tweets.columns
# df_count_tweets.columns = ['count']
# df_count_tweets.sort_index()


#Plotting scatterplot of lat/longs
df.head()

df['lon'].unique()
df.plot.scatter(x='lat',y='lon', alpha=0.4,title="Scatter plot of tweet locations within a 5mi Radius of Eric's Office")


# Scraping new tweets with search terms

# Set a Lat Lon
latlng = '42.359416,-71.093993' # Eric's office (ish)
# Set a search distance
radius = '5mi'
# See tweepy API reference for format specifications
geocode_query = latlng + ',' + radius
# RESET set output file location
file_name = 'data/climatetweets.json'
# set threshold number of Tweets. Note that it's possible
# to get more than one
t_max = 2000

#define the search terms
s1 = 'climate'


climate_tweets = get_tweets(
  search_term = s1,
  geo = geocode_query,
  tweet_max = t_max,
  write = True,
  out_file = file_name
)

climate_tweets.to_json('data/climatetweets.json')
climate_df = pd.read_json('data/climatetweets.json')
#checking for climate in tweets
# climate_df['content'].unique


boston_clist = climate_df[climate_df['location'].str.contains("Boston", case=False)]['location']
climate_df['location'].replace(boston_clist, 'Boston, MA', inplace = True)

#check that it's been replaced
# boston_list.value_counts()
climate_df['location'].value_counts()

cambridge_clist = climate_df[climate_df['location'].str.contains("Cambridge", case=False)]['location']
mass_clist = climate_df[climate_df['location'].str.contains("Massachusetts", case=False)]['location']
usa_clist = climate_df[climate_df['location'].str.contains("United States", case=False)]['location']
usa2_clist = climate_df[climate_df['location'].str.contains("U.S.A", case=False)]['location']
texas_clist = climate_df[climate_df['location'].str.contains("Texas", case=False)]['location']
medford_clist = climate_df[climate_df['location'].str.contains("Medford", case=False)]['location']
ny_clist = climate_df[climate_df['location'].str.contains("New York", case=False)]['location']
sville_clist = climate_df[climate_df['location'].str.contains("Somerville", case=False)]['location']
cali_clist = climate_df[climate_df['location'].str.contains("California", case=False)]['location']
wash_clist = climate_df[climate_df['location'].str.contains("Washington", case=False)]['location']
flor_clist = climate_df[climate_df['location'].str.contains("Florida", case=False)]['location']
ne_clist = climate_df[climate_df['location'].str.contains("New England", case=False)]['location']
penn_clist = climate_df[climate_df['location'].str.contains("Pennsylvania", case=False)]['location']
oh_clist = climate_df[climate_df['location'].str.contains("Ohio", case=False)]['location']
planet_clist = climate_df[climate_df['location'].str.contains("Earth", case=False)]['location']


climate_df['location'].replace(cambridge_clist, 'Cambridge, MA', inplace = True)
climate_df['location'].replace(mass_clist, 'Massachusetts', inplace = True)
climate_df['location'].replace(usa_clist, 'USA', inplace = True)
climate_df['location'].replace(usa2_clist, 'USA', inplace = True)
climate_df['location'].replace(texas_clist, 'Texas', inplace = True)
climate_df['location'].replace(medford_clist, 'Medford, MA', inplace = True)
climate_df['location'].replace(ny_clist, 'New York, NY', inplace = True)
climate_df['location'].replace(sville_clist, 'Somerville, MA', inplace = True)
climate_df['location'].replace(cali_clist, 'California', inplace = True)
climate_df['location'].replace(wash_clist, 'Washington, DC', inplace = True)
climate_df['location'].replace(flor_clist, 'Florida', inplace = True)
climate_df['location'].replace(ne_clist, 'New England', inplace = True)
climate_df['location'].replace(penn_clist, 'Pennsylvania, PA', inplace = True)
climate_df['location'].replace(oh_clist, 'Ohio', inplace = True)
climate_df['location'].replace(planet_clist, 'Earth', inplace = True)

climate_df['location'].value_counts()

#Remove missing tweet locations
climate_clean=climate_df[climate_df['location'] != ""]
climate_clean['location'].value_counts()

climate_clean
#Plotting scatterplot of lat/longs
climate_df.head()


climate_df['lon'].unique()
climate_df.plot.scatter(x='lat',y='lon', alpha=0.4,title="Scatter plot of 'climate' tweets within a 5mi Radius of Eric's Office")


#Datasets to csv files
# Note: Did not delete duplicates because the locations are not duplicated while RT'd.
# Note: Cleaned only the locations that had more than 5 instances logged

cleaner_tweets.to_csv('twitter_data.csv', sep=',', encoding='utf-8')
climate_clean.to_csv('climate_data.csv', sep=',', encoding='utf-8')
