# TwitterAPI-Googlecloud
#miniproject1
#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta
#modified by Sichun Hao

import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = ""                      #"Enter the consumer_key"
consumer_secret = ""                   #"Enter the consumer_secret"
access_key = ""                        #"Enter the access_key"
access_secret = ""                     #"Enter the access_secret"


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
    for status in alltweets:
        print(status.text)

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@realDonaldTrump")


for i in range():
#通过url存下图片 图片信息的url 在media组中。找到即可。用到skimage读取信息
    from skimage import io
    image=io.imread('提取到的图片链接http://pbs.twimg.com/media/DEOBBJJU0AATl3e.jpg')
    io.imshow(image)
    io.imsave('t.jpg',image)
    io.show()
