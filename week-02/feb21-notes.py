import pandas as pd
import numpy as np
import matplotlib 
%matplotlib inline

#Creating an object literal without any content; creating a Data frame with nothing in it!!
df = pd.DataFrame()
print(df)

#storing list
df['name'] = ['Bilbo', 'Frodo', 'Samwise']
df
#Assigning attributes; name the column height and create entries
df.assign(height = [0.5,0.4,0.6])

#most data is not created this way :P.....
#week 3 scripts can scrape things from AWS locker
#comma separated value, each element separated by a comma; telling the code that the separater is the comma

# can specifiy the file in the line => df = pd.read_csv('week-03/data/skyhook_2017-07.csv', sep=',')
#or can change the working directory
import os
os.chdir('week-03')
df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

#Dataframes head method to print out the first couple of rows, 5 rows
df.head()

df.shape #returns paired values; shows to length and width; # of rows and # of columns
df.shape[1] #returns 2nd value ie. columns
df.columns #returns all the column names
df['cat_name'].unique() #returns the different values in that columns
df['cat_name']
df.cat_name
#bracket syntax >, but some column names have function ex. df.count; count is a function!!
#Knowing about the data set, remember in the hours, theres 168 in the week but in python it's 0-167

#ask where the hour column is 158
df['hour'] == 158 # this gets a really long list of true/false values; array of true false values is called a mask and tested for each rows
#We want to pass the mask to the dataframe so that it creates a new set

one_fifty_eight = df[df['hour'] == 158]
one_fifty_eight.shape
#where hour ==158 is true, store the rows in the data frame that are true

df[(df['hour'] == 158) & (df['count'] > 50)] #query only asks, does not overwrite
#using the & in pandas; pandas conventions =>
and &
or |
not !

df[(df['hour'] == 158) & (df['count'] > 50)].shape
#number of people on bastille day/check ins
bastille = df[(df['date'] == '2017-07-14')]
bastille.head()
bastille.shape

#we want to find those who were more active than average on bastille day
bastille['count'] > bastille['count'].mean() #returns a mask that gives me those rows where count > mean of that count column is true
lovers_of_bastille = bastille['count'] > bastille['count'].mean() #passing into the variable

lovers_of_bastille = bastille[bastille['count'] > bastille['count'].mean()]
lovers_of_bastille.describe()
lovers_of_bastille['count'].describe()

#Groupby creates summary statistics of a given columns and criteria
df.groupby('date')['count'].sum().plot() #given unique dates, sums the count columns for that date

df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()

df[df['count'] == df['count'].max()]

df['hour'].unique
july_second = df[df['date'] == '2017-07-02']

july_second.groupby('hour')['count'].sum() #there's spill over the actually date, so we need to make this more useful

#Change the date column into something useful
df['date_new'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
#built in pandas method that takes the input and turns it into a readable time stamp, %y says look for 4 numbers, etc look at documentation

#hours of the week divided by 7 equals the set of hours that is that specific day...
#we want to know what day of the week it is
df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1) #lambda means i am defining my own function run on every element in date_new
#take the value, adds 1; weekday function is Monday to Sunday and we need it to be Sunday to Saturday
#in our data, the 0 hour is sunday, and the 0 weekday it's the monday, so we add the 1 to weekday

#we lose 0 and gain seven so we replace 7 with 0:
df['weekday'].replace(7,0,inplace = True)

# we want to drop columns outside of a 24-hour window
for i in range(0,168,24):#taking the hours and iterating them in 24s
    dr.drop(df[df['weekday'] == (i/24)]) & #limits to returned rows that are associated with given weekday value
    (
    (df['hour']) < i | df['hour'] > i + 24 #dropping hours outside of the bottom of this range or 24 hours above the range
    #but also, time is in GMT but Boston is 5 hours behind

    ])




    )
