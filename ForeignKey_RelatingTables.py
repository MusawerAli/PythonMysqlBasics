import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="root",
    database="PythonTestDatabase"
)

mycursor = db.cursor()
users = [("Musawer","1234"),
    ("ALi","321")]

users_score=[(23,43),
    (43,65)]


Q1 = "CREATE Table Users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),passwd VARCHAR(50))"
Q2 = "CREATE Table Scores(userId int PRIMARY KEY,FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

# mycursor.execute(Q1)
# mycursor.execute(Q2)

# mycursor.execute("SHOW TABLES")
Q3 = "INSERT INTO Users(name,passwd) VALUES (%s,%s)"
Q4 = "INSERT INTO Scores(userId,game1,game2) VALUES(%s,%s,%s)"


for x, user in enumerate(users):
    mycursor.execute(Q3,user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4,(last_id,)+ users_score[x])
db.commit()

mycursor.execute("SELECT * from Scores")
for x in mycursor:
    print(x)
    