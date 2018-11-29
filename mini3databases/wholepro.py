#!/usr/bin/env python
# encoding: utf-8
# author SichunHao
#export GOOGLE_APPLICATION_CREDENTIALS="/home/ece-student/601_mini1/My First Project-ab2764d710b6.json"
import tweepy #https://github.com/tweepy/tweepy
import json
import os,sys,ffmpeg
import pymysql
import pymongo
#import Image,ImageDraw,ImageFont
#from django import Image
# Twitter API credentials
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
consumer_key = ""                                       #"Enter the consumer_key"
consumer_secret = ""           #"Enter the consumer_secret"
access_key = ""                #"Enter the access_key"
access_secret = ""                  #"Enter the access_secret"
from skimage import io
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

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
		new_tweets = api.user_timeline(screen_name = screen_name,count=5,max_id=oldest)
        
		#save most recent tweets
		alltweets.extend(new_tweets)
        
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		if(len(alltweets) > 20):
			break
		#print ("...%s tweets downloaded so far" % (len(alltweets)))

	file = open('tweet.json', 'w')
	print ("Writing tweet objects to JSON please wait...")
	j=1
        #picurl=[0 in range(len(alltweets))]
	for status in alltweets:
		json.dump(status._json, file, sort_keys=True, indent=4)
		if 'media' in status.entities:
			print(status.entities["media"][0]["media_url"])
			image=io.imread(status.entities["media"][0]["media_url"])
			io.imsave('%03d.jpg'%(j),image)
			j=j+1
		#else:


		

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("@AngelAlessandra")
	import io
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	for i in range(1,25):
	# The name of the image file to annotate
		file_name = os.path.join(os.path.dirname(__file__),'%03d.jpg'%(i))
		font=ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 30)#font
		im=Image.open(file_name)#drawopen
		
		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations
		
		
		print('image%dlabels:'%i)
		j=1
		for label in labels:
			j=j+1
			print(label.description)
			print(label.score)
			draw=ImageDraw.Draw(im)
			loca=j*30
			draw.text((50,loca),label.description,(255,0,0),font=font)
			draw=ImageDraw.Draw(im)
			im.save('%03d.jpg'%(i))


os.system("ffmpeg -r 1 -f image2 -i %3d.jpg -s 1200x800 models.mp4")
