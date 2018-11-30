#!/usr/bin/env python
# encoding: utf-8
# author SichunHao
#export GOOGLE_APPLICATION_CREDENTIALS="/home/ece-student/601_mini1/My First Project-ab2764d710b6.json"
import collections
import tweepy #https://github.com/tweepy/tweepy
import json
import os,sys,ffmpeg
import pymysql
import pymongo
import PIL
import datetime
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

def get_all_tweets(screen_name,tweetsnumber):
    #Twitter only allows access to a users most recent 3240 tweets with this method
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	#initialize a list to hold all the tweepy Tweets
	alltweets = []    
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=tweetsnumber)
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
		if(len(alltweets) > tweetsnumber):
			break
		#print ("...%s tweets downloaded so far" % (len(alltweets)))

	file = open('tweet.json', 'w')
	print ("Writing tweet objects to JSON please wait...")
	j=1
        #picurl=[0 in range(len(alltweets))]
	for status in alltweets:
		json.dump(status._json, file, sort_keys=True, indent=4)
		if 'media' in status.entities:
			#---------------links-----------------------------------
			print(status.entities["media"][0]["media_url"])
			image=io.imread(status.entities["media"][0]["media_url"])
			io.imsave('%03d.jpg'%(j),image)
			j=j+1
		#else:
			#if fault exist, the instruction can be decided here

		

if __name__ == '__main__':
	#pass in the username of the account you want to download
	username=input("please type in user's name:")
	tweetname=input("please type in the name you want to search(eg.@AngelAlessandra):")
	tweetsnumber=input("please input the number of tweets you want to know:")
	tweetsnumber=int(tweetsnumber)
	get_all_tweets(tweetname,tweetsnumber)


	import io
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	for i in range(1,2*tweetsnumber):
		count=0
		try:
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

			count=count+1
			#parameters need to be stored
			for i in len(labels):
				if(i==0):
					keyword1=labels[0]
				elif(i==1):
					keyword2=labels[1]
				elif(i==2):
					keyword3=labels[2]
				elif(i==3):
					keyword4=labels[3]
				elif(i==4):
					keyword5=labels[4]	
				elif(i==5):
					keyword6=labels[5]
			
				#mongodb
				myclient = pymongo.MongoClient("mongodb://localhost:27017/")
				mydb = myclient["mini3mongo"]
				mycol = mydb["tweetsinquiry"]
				record = {"time":datetime.datetime.now(),"username":username,"tweetname":tweetname,"tweetsnumber":tweetsnumber,
						"keyword1":keyword1,"keyword2":keyword2,"keyword3":keyword3,"keyword4":keyword4,
						"keyword5":keyword5,"keyword6":keyword6}
				x=mycol.insert_one(record)
				#mysql  
				db= pymysql.connect("localhost","root",password here,"601mini3")  
				cursor = db.cursor()  
				sql="INSERT INTO tweetsinquiry value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				try:
					cursor.execute(sql,[username,tweetname,tweetsnumber,keyword1,keyword2,keyword3,keyword4,keyword5,keyword6])
				# submit to database
					db.commit()
				except:
					db.rollback()
				db.close()
			# find the number of images or the keywords exist most
			filename = 'storedatabase1.txt'
			with open(filename,'a') as f: 
				# 'a': append,add data to original file
				f.write("username"+username+"\n")
				f.write("tweetname"+tweetname+"\n")
				f.write("tweetsnumber"+tweetsnumber+"\n")
				f.write("imagenumber"+count+"\n")
				f.write(keyword1+"\n")
				f.write(keyword2+"\n")
				f.write(keyword3+"\n")
				f.write(keyword4+"\n")
				f.write(keyword5+"\n")
				f.write(keyword6+"\n")
			'''#users information
			filename = 'storedatabase2.txt'			
			with open(filename,'a') as f: 
				# 'a': append,add data to original file
				f.write("username"+username+"\n")
				f.write("tweetname"+tweetname+"\n")
				f.write("tweetsnumber"+tweetsnumber+"\n")
				f.write("imagenumber"+count+"\n")
			'''
		except:
			pass



os.system("ffmpeg -r 1 -f image2 -i %3d.jpg -s 1200x800 models.mp4")
#overal number & keyword
with open('storedatabase1.txt') as file1:
	str1=file1.read().split()
	print ("orinial dataset:\n %s"% str1)
	print ("\ntimes for each word：\n %s" % collections.Counter(str1))
	#print collections.Counter(str1)['the word we want to search']
