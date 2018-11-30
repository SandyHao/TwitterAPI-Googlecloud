Here is the program for mini project 3<br>
Using both mysql & mongodb databases.<br>

Installation MySQL
-

Connect to MySQL
-
		db= pymysql.connect("localhost","root",passwordhere,"601mini3")  
		cursor = db.cursor()  

Installation MongoDB
-
* download setup package from official site：https://www.mongodb.com/download-center#community<br>
* setup the application as instruction<br>
* create data folder in the same root<br>
* execute:  "root"\mongodb\bin\mongod --dbpath "root"\mongodb\data\db(the root could be changed)<br>
* create config file; eg. content show as bellow<br>
	```
	systemLog:<br>
	    destination: file<br>
	    path: c:\data\log\mongod.log<br>
	storage:<br>
	    dbPath: c:\data\db<br>
	```
* setup & setting: C:\mongodb\bin\mongod.exe --config "C:\mongodb\mongod.cfg" --install
* start: net start MongoDB<br>
* stop: net stop MongoDB

Connect to MongoDB
-
		myclient = pymongo.MongoClient("mongodb://localhost:27017/")
		mydb = myclient["mini3mongo"]
		mycol = mydb["tweetsinquiry"]

Differents between mysql and mongodb
-
mysql                | mongodb
---------------------| ---------------------
database             | database
table                | collection
row                  | document
column               | field
index                | index
table joins          | null
primary key          | primary key
