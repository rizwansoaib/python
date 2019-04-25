import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="rizwan",
  passwd="Rizwan@111",
  database="knit"
)

#mysql_query("UPDATE ATTENDENCE SET ATTENDENCE=ATTENDENCE+1 WHERE NAME = "gullu"")

mycursor = mydb.cursor()
mycursor.execute("SELECT ATTENDENCE FROM student WHERE NAME='gullu'")

myresult = mycursor.fetchall()
crnt=myresult[0][0]
print(crnt)
crnt+=1
mycursor.execute("UPDATE student SET ATTENDENCE ="+str(crnt)+ " WHERE NAME = 'gullu'")

mydb.commit()
