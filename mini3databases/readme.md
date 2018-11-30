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
