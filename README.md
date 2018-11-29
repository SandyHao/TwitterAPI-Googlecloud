# TwitterAPI-Googlecloud
miniproject1
-
set up environment:
1. register google API to get keys<br>
2. use "pip3 install google-cloud-vision" to install google cloud API<br>

before running:
1. input twitter api keys in downloading.py & whole.py<br>
2. before using gcvapi.py & whole.py      
   if Linux run<br>
   export GOOGLE_APPLICATION_CREDENTIALS="/home/xxx/xxx/xxx.json"<br>
   else if Windows run<br>
   set GOOGLE_APPLICATION_CREDENTIALS="/home/xxx/xxx/xxx.json"<br>
   it is the route for google cloud vision api token

contents: seperate the project into 3 section
1. downloading.py_download images from twitter
2. ffmpegtrans.py_combine images into video
3. gvcapi.py_using google cloud vision to figure out the items in video
4. for all the function, run whole.py

change the xxx to the name on twitter(the one you want to know)  "get_all_tweets("@xxx")"in main<br>

Here is the result of a labeled image.
![](https://github.com/SandyHao/TwitterAPI-Googlecloud/blob/master/002.jpg)
