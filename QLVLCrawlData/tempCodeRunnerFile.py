con = mysql.connector.connect(user='root', host='localhost', password='1234', database='pbl3')
cursor = con.cursor()
sql = "INSERT INTO industry (name) VALUES('haha')"

cursor.execute(sql)
con.commit()