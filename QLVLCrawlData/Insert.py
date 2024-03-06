
import mysql.connector

connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
cursor = connection.cursor()
 

sql = "INSERT INTO industry(name) VALUES ('haha')"
cursor.execute(sql)


#cursor.execute(sql)

connection.commit()
connection.close()

# l = [1, 2, 3, 4, 5, 6, 7]

# print(l[3:6]) # include 3 , exclude 6
# a = [2, 1]
# a.extend(l[3:6])
# print(len(a))




