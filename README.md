# TwitterAPI-Googlecloud
#miniproject1

before running:
1. input twitter api keys in downloading.py & whole.py
2. before using gcvapi.py & whole.py      
   run             export GOOGLE_APPLICATION_CREDENTIALS="/home/xxx/xxx/xxx.json"
   it is the route for google cloud vision api token

contents: seperate the project into 3 section
1. downloading.py_download images from twitter
2. ffmpegtrans.py_combine images into video
3. gvcapi.py_using google cloud vision to figure out the items in video
4. for all the function, run whole.py

change the xxx to the name on twitter(the one you want to know)  "get_all_tweets("@xxx")"in main
