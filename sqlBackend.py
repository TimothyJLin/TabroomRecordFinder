import mysql.connector
mydb = mysql.connector.connect(
  host="mysql-project1-records-of-debaters.g.aivencloud.com",
  user="avnadmin",
  password="AVNS_4XSzs7y1KtaqGb4e-V3",
  database="defaultdb",
  port=21468,
#environ['password'].
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM localentries WHERE name='shion lee'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
#print(mydb)