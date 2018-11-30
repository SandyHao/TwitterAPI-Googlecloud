Here is the program for mini project 3<br>
Using both mysql & mongodb databases.<br>

Installation MySQL
-
* download setup package from official site：https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.11-winx64.zip <br>
* set my.ini file<br>
	```
	[mysql]
	default-character-set=utf8

	[mysqld]
	port = 3306
	# set up root
	basedir=C:\\web\\mysql-8.0.11
	# data root
	# datadir=C:\\web\\sqldata
	max_connections=20
	character-set-server=utf8
	default-storage-engine=INNODB
	```
* use admin cmd
* change to bin folder of mysql
* get initial password
	```
	mysqld --initialize --console
	```
* install mysql
	```
	mysqld install
	```
* start mysql
	```
	net start mysql
	```
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
* we need to reset the password after login

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
