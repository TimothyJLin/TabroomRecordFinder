import mysql.connector
def findDebater(debateName, debateSchool):
  print("sqlbackend accessed!")
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
  debaterArray=[]

  for element in myresult[0]:
    debaterArray.append(element)
  print("string of array: "+str(debaterArray))
  return debaterArray
#  return debaterArray
#  return JSON.stringify(myresult)

#look at this for parsing information ideas
  for x in myresult:
    print(x)
  #print(mydb)
#findDebater("test", "run")
