import pymysql  

username="Mac"
tweetname="sichun"
tweetsnumber=20
keyword1="model"
keyword2="beauty"
keyword3="tall"
keyword4="hair"
keyword5= "curly"
keyword6="children"
#connect to mysql
db= pymysql.connect("localhost","root","Lianzhiji##4","601mini3")  
# use cursor()  
cursor = db.cursor()  
sql="INSERT INTO tweetsinquiry value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# insert
try:
    cursor.execute(sql,[username,tweetname,tweetsnumber,keyword1,keyword2,keyword3,keyword4,keyword5,keyword6])
   # submit to execute
    db.commit()
except:
   # if error
   db.rollback()
# close database
db.close()

