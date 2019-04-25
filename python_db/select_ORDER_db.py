import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="rizwan",
  passwd="",
  database="knit"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM student ORDER by ATTENDENCE DESC")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
