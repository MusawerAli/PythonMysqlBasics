import mysql.connector
from datetime import datetime
db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="root",
    database="PythonTestDatabase"
)

mycursor = db.cursor()

#Make Tables
#mycursor.execute("CREATE Table Person (name VARCHAR(50),age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("CREATE TABLE Test(name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F','0') NOT NULL, id int PRIMARY KEY NOT NULL)")

#Insert Data
# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("Ali",21))
# db.commit()
#mycursor.execute("SELECT * FROM Person"


#SELECT DATA
# mycursor.execute("INSERT INTO Test(name,created,gender) VALUES(%s,%s,%s)",("Ali",datetime.now(),"M"))
# mycursor.execute("SELECT * FROM Test")
# db.commit()
# mycursor.execute("DESCRIBE Person")
# mycursor.execute("DESCRIBE Test")
# print(mycursor.fetchall())


# mycursor.execute("ALTER TABLE Test ADD COLUMN food varchar(50) not null")
mycursor.execute("ALTER TABLE Test drop food")
# for x in mycursor:
#     print(x)
