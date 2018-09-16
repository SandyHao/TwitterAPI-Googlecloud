#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json


# Twitter API credentials
consumer_key = "YeVl6m88wogA0BD3JdYJ82SMN"                                               #"Enter the consumer_key"
consumer_secret = "GG3nW2loOVBXT2q1DlRcyTdufEVzTQ4tz2DYJnd8URdcv6SfJV"                   #"Enter the consumer_secret"
access_key = "1039021907595673600-ZlCCSvJGRJdjLvpKzisTa51rjhTxmO"                        #"Enter the access_key"
access_secret = "f3SyAxg4kcL7KBG04cIW4Vv9pOecUPRkUjXGnbutqMvcR"                          #"Enter the access_secret"
from skimage import io

def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print "...%s tweets downloaded so far" % (len(alltweets))

    file = open('tweet.json', 'w')
    print "Writing tweet objects to JSON please wait..."
    j=1
    #picurl=[0 in range(len(alltweets))]
    for status in alltweets:
        json.dump(status._json, file, sort_keys=True, indent=4)
        print(status.entities["media"][0]["media_url"])
        image=io.imread(status.entities["media"][0]["media_url"])
        io.imshow(image)
        io.imsave('%d.jpg'%(j),image)
        j=j+1

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@SichunH")



